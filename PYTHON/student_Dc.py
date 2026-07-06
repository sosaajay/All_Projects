print("\nWelcome to the Student Data Organizer!")
students = []

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display all Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter student details:")
        st = {
            "id": int(input("Student ID: ")),
            "name": input("Name: "),
            "age": int(input("Age: ")),
            "grade": input("Grade: "),
            "dob":input("Date of Birth (dd-mm-yyyy): "),
            "subjects": input("Subjects (comma-separated): ").split(",")
        }
        students.append(st)
        print("\nStudent added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("\nNo student records found!")
        else:
            print("\n--- Display All Students ---")
            for st in students:
                print(f"Student ID: {st['id']} | Name: {st['name']} | Age: {st['age']} | Grade: {st['grade']} | DOB: {st['dob']} | Subjects: {st['subjects']}")

    elif choice == 3:
        upd = False
        id_to_update = int(input("\nEnter student ID to update: "))
        for st in students:
            if st["id"] == id_to_update:
                st["name"] = input("New Name: ")
                st["age"] = int(input("New Age: "))
                st["grade"] = input("New Grade: ")
                st["dob"] = input("New Date of Birth (dd-mm-yyyy): ")
                st["subjects"] = input("New Subjects (comma-separated): ")
                print("\nStudent updated successfully!")
        if upd==False:
            print("student deteils not faund")       
        

    elif choice == 4:
        delt=True
        id_to_delete = int(input("\nEnter student ID to delete: "))
        for st in students:
            if st["id"] == id_to_delete:
                students.remove(st)
                print("Student deleted successfully!")
        if delt==False:
            print("student details not faund")        
        

    elif choice == 5:
        find = False
        if len(students) == 0:
            print("\nNo student records found!")
        else:
            id_to_view = int(input("\nEnter student ID to view subjects: "))
            for st in students:
                if st["id"] == id_to_view:
                    print(f"\nSubjects offered by {st['name']} (ID: {st['id']}):")
                    print((st["subjects"]))
                    find=True
            if find==False:
                print("student not faund")    


    elif choice == 6:
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("\nInvalid choice! Please try again.")
