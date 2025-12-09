import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.df = None  
  
    def loaddata(self):
        try:
            file = input("\nEnter CSV file path: ")
            self.df = pd.read_csv(file)
            print("\nDataset loaded successfully!\n")
            print(self.df.head())
        except:
            print("\nError: Unable to load file. Please check path.\n")

    def exploredata(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")

            ch = int(input("Enter your choice: "))

            
            if ch == 1:
                print("\n===== First 5 rows =====")
                print(self.df.head())

            
            elif ch == 2:
                print("\n===== Last 5 rows =====")
                print(self.df.tail())

            elif ch == 3:
                print("\n===== Column Names =====")
                print(list(self.df.columns))

            
            elif ch == 4:
                print("\n===== Data Types =====")
                print(self.df.dtypes)

            
            elif ch == 5:
                print("\n===== Basic Info =====")
                print(self.df.info())

           
            elif ch == 6:
                return

            else:
                print("Invalid choice! Please try again.")

    def dataframeoperations(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Select a specific column")
            print("2. Filter rows based on a condition")
            print("3. Add a new column")
            print("4. Delete a column")
            print("5. Sort data by column")
            print("6. Show updated DataFrame")
            print("7. Back to Main Menu")

            ch = input("Enter your choice: ")

            if ch == "1":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(self.df[col])
                else:
                    print("Column not found!")

            elif ch == "2":
                col = input("Enter column name to filter: ")
                if col not in self.df.columns:
                    print("Column not found!")
                    continue
                val = input("Enter value to match: ")
                print(self.df[self.df[col] == val])

            elif ch == "3":
                col = input("Enter new column name: ")
                val = input("Enter value for all rows: ")
                self.df[col] = val
                print("Column added successfully!")

            elif ch == "4":
                col = input("Enter column name to delete: ")
                if col in self.df.columns:
                    self.df.drop(columns=[col], inplace=True)
                    print("Column deleted!")
                else:
                    print("Column not found!")

            elif ch == "5":
                col = input("Enter column name to sort: ")
                if col in self.df.columns:
                    self.df = self.df.sort_values(by=col)
                    print("Data sorted successfully!")
                else:
                    print("Column not found!")

            elif ch == "6":
                print("\n=== Updated DataFrame ===")
                print(self.df)

            elif ch == "7":
                return

            else:
                print("Invalid choice!")

    def handlemissingdata(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to Main Menu")

            ch = input("Enter your choice: ")

        
            if ch == "1":
                missing = self.df[self.df.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print("\nRows with missing values:")
                    print(missing)

            elif ch == "2":
                numcols = self.df.select_dtypes(include=['float64', 'int64'])
                if numcols.empty:
                    print("No numeric columns available!")
                else:
                    self.df[numcols.columns] = numcols.fillna(numcols.mean())
                    print("Missing values filled with mean!")

            elif ch == "3":
                before = len(self.df)
                self.df.dropna(inplace=True)
                after = len(self.df)
                print(f"Dropped {before - after} rows containing missing values.")

           
            elif ch == "4":
                val = input("Enter value to replace missing values with: ")
                self.df.fillna(val, inplace=True)
                print("Replacement completed!")

            elif ch == "5":
                return

            else:
                print("Invalid choice!")

    def descriptivestatistics(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Generate Descriptive Statistics ==")
            print("1. Show summary statistics")
            print("2. Show statistics for a specific column")
            print("3. Show correlation matrix")
            print("4. Show unique values for a column")
            print("5. Back to Main Menu")

            ch = input("Enter your choice: ")

            
            if ch == "1":
                print("\n===== Summary Statistics =====")
                print(self.df.describe(include='all'))

    
            elif ch == "2":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(f"\n===== Statistics for '{col}' =====")
                    print(self.df[col].describe())
                else:
                    print("Column not found!")

            
            elif ch == "3":
                numericdf = self.df.select_dtypes(include=['float64', 'int64'])
                if numericdf.empty:
                    print("No numeric columns available for correlation.")
                else:
                    print("\n===== Correlation Matrix =====")
                    print(numericdf.corr())

        
            elif ch == "4":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(f"\nUnique values in '{col}':")
                    print(self.df[col].unique())
                else:
                    print("Column not found!")

            elif ch == "5":
                return

            else:
                print("Invalid choice! Try again.")
                
   
    def visualizedata(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Line Plot")
            print("2. Bar Plot")
            print("3. Histogram")
            print("4. Scatter Plot")
            print("5. Heatmap (Correlation)")
            print("6. Stack Plot")
            print("7. Back to Main Menu")

            ch = input("Enter your choice: ")

           
            if ch == "1":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.plot(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Line Plot: {y} vs {x}")
                    plt.grid()
                    plt.show()
                else:
                    print("Invalid columns!")

            elif ch == "2":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.bar(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Bar Chart: {y} by {x}")
                    plt.show()
                else:
                    print("Invalid columns!")

            
            elif ch == "3":
                col = input("Enter column for histogram: ")
                if col in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.hist(self.df[col], bins=20)
                    plt.xlabel(col)
                    plt.title(f"Histogram of {col}")
                    plt.show()
                else:
                    print("Column not found!")

            
            elif ch == "4":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.scatter(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Scatter Plot: {y} vs {x}")
                    plt.show()
                else:
                    print("Invalid columns!")

            elif ch == "5":
                numeric_df = self.df.selectdtypes(include=['int64', 'float64'])
                if numeric_df.empty:
                    print("No numeric columns available for heatmap.")
                else:
                    plt.figure(figsize=(10,6))
                    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
                    plt.title("Correlation Heatmap")
                    plt.show()

            elif ch == "6":
                print("\nEnter multiple numeric columns for stack plot (comma separated):")
                print("Example: sales,profit,expenses")

                columns = input("Enter column names: ").replace(" ", "").split(",")

                missing = [c for c in columns if c not in self.df.columns]
                if missing:
                    print("These columns do not exist:", missing)
                    continue

                nonnumeric = [c for c in columns if self.df[c].dtype not in ['int64', 'float64']]
                if nonnumeric:
                    print("Non-numeric columns cannot be used:", nonnumeric)
                    continue

                xcol = input("Enter X-axis column: ")

                if xcol not in self.df.columns:
                    print("X-axis column not found!")
                    return

                plt.figure(figsize=(10,6))
                plt.stackp
                
    def savevisualization(self):
        if self.lastplot is None:
            print("\nNo visualization found! Create a plot first.\n")
            return

        print("\n== Save Visualization ==")
        filename = input("Enter filename (e.g., chart.png): ")

        try:
            self.last_plot.savefig(filename)
            print(f"Visualization saved successfully as '{filename}'\n")
        except Exception as e:
            print("Error saving file:", e)

def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n==============================")
        print(" Sales Data Analysis Program ")
        print("==============================")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Values")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.loaddata()

        elif choice == "2":
            analyzer.exploredata()
            
        elif choice == "3":
            analyzer.dataframeoperations()
        
        elif choice == "4":
            analyzer.handlemissingdata()
 
        elif choice == "5":
            analyzer.descriptivestatistics()
    
        elif choice == "6":
            analyzer.visualizedata()
        
        elif choice == "7":
            analyzer.savevisualization()

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Feature not added yet!")

main()
