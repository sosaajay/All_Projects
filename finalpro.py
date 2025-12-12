import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class HappinessDashboard:
    """
    A dashboard to analyze the World Happiness Dataset.
    Provides statistical insights and visualizations.
    """

    REQUIRED_COLUMNS = [
        'Country', 'Regional indicator', 'Happiness score',
        'GDP per capita', 'Social support', 'Healthy life expectancy',
        'Freedom to make life choices', 'Year'
    ]

    def __init__(self):
        self.df = None

    # ------------------------- DATA LOADING ------------------------- #

    def load_data(self, file_path):
        """Load dataset and validate required columns"""
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            raise ValueError(f"Error loading file: {e}")

        missing = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        df = df.dropna(subset=self.REQUIRED_COLUMNS)
        self.df = df
        print("\n✔ Dataset loaded and validated successfully!")

    # ------------------------- CALCULATIONS ------------------------- #

    def calculate_statistics(self):
        """Generate key summary statistics"""
        if self.df is None:
            raise ValueError("Dataset not loaded!")

        region_avg = self.df.groupby("Regional indicator")['Happiness score'].mean()
        happiest_country = self.df.loc[self.df['Happiness score'].idxmax(), 'Country']
        avg_life = self.df['Healthy life expectancy'].mean()

        return {
            "Avg Happiness by Region": region_avg.to_dict(),
            "Happiest Country": happiest_country,
            "Avg Life Expectancy": round(avg_life, 2)
        }

    # ------------------------- FILTERING ------------------------- #

    def filter_data(self, region=None, start_year=None, end_year=None):
        """Filter dataset by region and year"""
        if self.df is None:
            raise ValueError("Dataset not loaded!")

        filtered = self.df.copy()

        if region:
            filtered = filtered[filtered['Regional indicator'].str.lower() == region.lower()]

        if start_year and end_year:
            filtered = filtered[(filtered['Year'] >= start_year) & (filtered['Year'] <= end_year)]

        return filtered

    # ------------------------- VISUALIZATIONS ------------------------- #

    def plot_bar_chart(self):
        """Top 10 happiest countries"""
        top = self.df.nlargest(10, "Happiness score")
        plt.figure(figsize=(9, 5))
        sns.barplot(x='Happiness score', y='Country', data=top)
        plt.title("Top 10 Happiest Countries")
        plt.tight_layout()
        plt.show()

    def plot_line_graph(self):
        """Global happiness trend over years"""
        yearly = self.df.groupby("Year")['Happiness score'].mean()
        plt.figure(figsize=(8, 4))
        sns.lineplot(x=yearly.index, y=yearly.values, marker='o')
        plt.title("Global Happiness Trend Over Years")
        plt.xlabel("Year")
        plt.ylabel("Happiness Score")
        plt.tight_layout()
        plt.show()

    def plot_pie_chart(self):
        """Average happiness percentage by region"""
        region_avg = self.df.groupby("Regional indicator")['Happiness score'].mean()
        plt.figure(figsize=(6, 6))
        plt.pie(region_avg, labels=region_avg.index, autopct='%1.1f%%')
        plt.title("Happiness Score Distribution by Region")
        plt.tight_layout()
        plt.show()

    def plot_heatmap(self):
        """Correlation heatmap of key happiness factors"""
        corr = self.df[['Happiness score', 'GDP per capita', 'Social support',
                        'Healthy life expectancy', 'Freedom to make life choices']].corr()
        plt.figure(figsize=(7, 5))
        sns.heatmap(corr, annot=True, cmap="YlGnBu")
        plt.title("Factor Correlation Heatmap")
        plt.tight_layout()
        plt.show()


# =========================== MAIN PROGRAM =========================== #

def main():
    dashboard = HappinessDashboard()

    while True:
        print("\n========== GLOBAL HAPPINESS DASHBOARD ==========")
        print("1. Load Dataset")
        print("2. Show Summary Statistics")
        print("3. Filter Data")
        print("4. Bar Chart (Top Countries)")
        print("5. Line Chart (Yearly Trend)")
        print("6. Pie Chart (Regional Dist.)")
        print("7. Correlation Heatmap")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        try:
            if choice == '1':
                file_path = input("Enter dataset CSV path: ")
                dashboard.load_data(file_path)

            elif choice == '2':
                stats = dashboard.calculate_statistics()
                print("\n========== SUMMARY REPORT ==========")
                print("Happiest Country:", stats["Happiest Country"])
                print("Average Life Expectancy:", stats["Avg Life Expectancy"])
                print("\nAverage Happiness by Region:")
                for region, value in stats["Avg Happiness by Region"].items():
                    print(f"{region}: {value:.2f}")

            elif choice == '3':
                region = input("Region (leave blank for none): ").strip() or None
                s = input("Start Year: ").strip()
                e = input("End Year: ").strip()
                start = int(s) if s else None
                end = int(e) if e else None
                filtered = dashboard.filter_data(region, start, end)
                print(f"\nFiltered rows: {len(filtered)}")
                print(filtered.head())

            elif choice == '4':
                dashboard.plot_bar_chart()

            elif choice == '5':
                dashboard.plot_line_graph()

            elif choice == '6':
                dashboard.plot_pie_chart()

            elif choice == '7':
                dashboard.plot_heatmap()

            elif choice == '8':
                print("\nExiting Dashboard... Goodbye!")
                break

            else:
                print("⚠ Invalid choice! Please select 1-8.")

        except Exception as e:
            print(f"⚠ Error: {e}")


if __name__ == "__main__":
    main()
