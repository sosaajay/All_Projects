print("Welcome to data anaylzer and tranformer program \n" )

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)

def display_summary(record):
    print("\nData Summary:")
    print(f" - Tatal elements of data: {len(record)}")
    print(f" - Minimum value: {min(record)}")
    print(f" - Maximum value: {max(record)}")
    print(f" - Sum of all value: {sum(record)}")
    print(f" - Average value : {sum(record) / len(record):}")
    
def stats(record):
    return min(record), max(record), sum(record), sum(record) / len (record)

record = []

while True:
    print("\n Main menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. calcate factorial")
    print("4. Filter Data by threshold")
    print("5. sort data")
    print("6. Display dataset statistict")
    print("7. Exit program\n")
    choice = int(input("Enter your choice: ")) 
    
    if choice == 1:
        raw = input("Enter data for a 1D array (separated by spaces): \n" )
        for i in raw.split():
            record.append(int(i))
            
        print("\n Data has been stored successfully! \n")
            
    elif choice == 2:
        if record:
            display_summary(record)
        else:
            print("No data to display.")
            
    elif choice == 3:
        print()
        num = int(input("Enter a number to calculate its factorial:"))
        print()
        print(f"Factorial of {num} is: {fact(num)}\n")  
        
    elif choice == 4:
        print()
        threshold = int(input("Enter a threshold value to filter out data above this value: \n"))
        filtered = [i for i in record if i > threshold]
        print(f"\n Filtered Data (values > {threshold}) : {filtered} \n")
        
    elif choice == 5:
        if record:
            ascending = sorted(record)
            descending = sorted(record, reverse=True)

            print(f"\nSorted data in Ascending order: {ascending}")
            print(f"Sorted data in Descending order: {descending}\n")
        else:
             print("No data to sort.")
        
    elif choice == 6:
        if record:
            min_value = min(record)
            max_value = max(record)
            total = sum(record)

            print("\n Dataset Statistics: \n")
            print(f" - Minimum value : {min_value}")
            print(f" - Maximum value : {max_value}")
            print(f" - Sum of all values : {total}")
            print(f" - Average value : {total / len(record):} \n")
        else:
            print("No data to display.")
    
            
            
    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.\n")