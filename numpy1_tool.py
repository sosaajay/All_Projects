import numpy as np

print("\nWelcome to the Numpy Analyzer 😊!")
print("===============================")

def create_array():
    print("\nSelect type of array to create:👍:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input🚨!")
        return None

    if choice == 1:
        size = int(input("Enter number of elements:👍:"))
        elements = list(map(int, input("Enter elements: ").split()))

        if len(elements) != size:
            print("Error: element count mismatch.🚨")
            return None
        
        arr = np.array(elements)
        print("\nArray created:🐻‍❄️:")
        print(arr)
        return arr

    elif choice == 2:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        print("Enter elements row wise separated by space:😀:")
        elements = list(map(int, input().split()))

        if len(elements) != rows * cols:
            print("Error: element count mismatch.🚨")
            return None

        arr = np.array(elements).reshape(rows, cols)
        print("\nArray created:😄")
        print(arr)
        return arr

    elif choice == 3:
        depth = int(input("Enter depth: "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = depth * rows * cols
        print(f"Enter {total} elements:")
        elements = list(map(int, input().split()))

        if len(elements) != total:
            print("Error: element count mismatch.🚨")
            return None

        arr = np.array(elements).reshape(depth, rows, cols)
        print("\nArray created:😊")
        print(arr)
        return arr

    else:
        print("Invalid choice!🚨")
        return None

def mathematical_operations(arr):
    print("\nChoose an operation:🤞:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))
    n = int(input("Enter number: "))

    print("\nResult:")
    if choice == 1:
        print(arr + n)
    elif choice == 2:
        print(arr - n)
    elif choice == 3:
        print(arr * n)
    elif choice == 4:
        if n == 0:
            print("Error: Cannot divide by zero.🚨")
        else:
            print(arr / n)
    else:
        print("Invalid choice!🚨")

def search_sort_filter(arr):
    print("\nSearch Sort and Filter:")
    print("1. Search")
    print("2. Sort")
    print("3. Filter (> value)")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element to search:😶‍🌫️:"))
        print("Positions:", np.where(arr == x))

    elif choice == 2:
        print("\nSorted array:")
        print(np.sort(arr, axis=None))

    elif choice == 3:
        limit = int(input("Enter limit: "))
        print("\nFiltered array:")
        print(arr[arr > limit])

    else:
        print("Invalid choice!🚨")

def aggregation_functions(arr):
    print("\nChoose aggregation/statistical operation:😊:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Max")
    print("5. Min")

    choice = int(input("Enter your choice:🤞:"))

    print("\nResult:")
    if choice == 1:
        print(np.sum(arr))
    elif choice == 2:
        print(np.mean(arr))
    elif choice == 3:
        print(np.median(arr))
    elif choice == 4:
        print(np.max(arr))
    elif choice == 5:
        print(np.min(arr))
    else:
        print("Invalid choice!🚨")

def combine_arrays(arr):
    print("\nCombine arrays:")
    print("1. Horizontal")
    print("2. Vertical")

    choice = int(input("Enter your choice: "))

    print("Enter elements for another array:🤞:")
    new = list(map(int, input("Enter elements: ").split()))
    arr2 = np.array(new)

    try:
        if choice == 1:
            print("\nCombined array (Horizontal):")
            print(np.hstack((arr, arr2)))

        elif choice == 2:
            print("\nCombined array (Vertical):")
            print(np.vstack((arr, arr2)))

        else:
            print("Invalid choice!🚨")

    except:
        print("Error: Shape mismatch.🚨")

def split_array(arr):
    print("\nSplit array:")
    print("1. Horizontal split")
    print("2. Vertical split")

    choice = int(input("Enter your choice: "))

    try:
        if choice == 1:
            print(np.hsplit(arr, 2))
        elif choice == 2:
            print(np.vsplit(arr, 2))
        else:
            print("Invalid choice!")
    except:
        print("Error: Cannot split evenly.🚨")

def main():
    arr = None

    while True:
        print("\nChoose an option:😇:")
        print("1. Create array")
        print("2. Mathematical operations")
        print("3. Search, sort, filter")
        print("4. Aggregation / Statistics")
        print("5. Combine arrays")
        print("6. Split arrays")
        print("7. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr = create_array()

        elif choice == 2 and arr is not None:
            mathematical_operations(arr)

        elif choice == 3 and arr is not None:
            search_sort_filter(arr)

        elif choice == 4 and arr is not None:
            aggregation_functions(arr)

        elif choice == 5 and arr is not None:
            combine_arrays(arr)

        elif choice == 6 and arr is not None:
            split_array(arr)

        elif choice == 7:
            print("Thank you for using the Numpy Multitool!😊")
            break

        else:
            print("Please create an array first!🫡")

main()
