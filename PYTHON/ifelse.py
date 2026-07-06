while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!")
    print()
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:\n")
        for i in range(1, a + 1):
            print("*" * i)    

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0

        for t in range(start, end + 1):
            if t % 2 == 0:
                print("Number", t, "is Even")
            else:
                print("Number", t, "is Odd")
            total += t

        print("\nSum of all numbers from", start, "to", end, "is:", total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Your choice is not here!")
