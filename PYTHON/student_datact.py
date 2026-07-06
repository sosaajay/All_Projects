print("\n🌟 Welcome to the Student Data Organizer 🌟")

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
            "id": input("Student ID: "),
            "Name": input("Name: "),
            "Age": int(input("Age: ")),
            "Grade": input("Grade: "),
            "Dob": input("Date of Birth (dd-mm-yyyy): "),
            "Subjects": input("Subjects (comma-separated): ").split(",")
        }
        students.append(st)
        print("\n✅ Student added successfully!")

    elif choice == 2:
        if not students:
            print("\nNo student records found!")
        else:
            print("\n--- 🧾 Student Records ---")
            for st in students:
                print(f"Student ID: {st['id']} | Name: {st['Name']} | Age: {st['Age']} | Grade: {st['Grade']} | DOB: {st['Dob']} | Subjects: {', '.join(st['Subjects'])}")

    elif choice == 3:
        update = input("\nEnter student ID to update: ")
        for st in students:
            if st["id"] == update:
                st["Name"] = input("New Name: ")
                st["Age"] = int(input("New Age: "))
                st["Grade"] = input("New Grade: ")
                st["Dob"] = input("New Date of Birth (dd-mm-yyyy): ")
                st["Subjects"] = input("New Subjects (comma-separated): ").split(",")
                print("\n✅ Student updated successfully!")
                break
        else:
            print("❌ Student not found!")

    elif choice == 4:
        delete = input("\nEnter student ID to delete: ")
        for st in students:
            if st["id"] == delete:
                students.remove(st)
                print("🗑️ Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == 5:
        all_subjects = set()
        for st in students:
            all_subjects.update(st["Subjects"])
        if all_subjects:
            print("\n📘 Subjects Offered by All Students:")
            print(", ".join(all_subjects))
        else:
            print("No subjects found!")

    elif choice == 6:
        print("\n👋 Thank you for using the Student Data Organizer!")
        break

    else:
        print("\n⚠️ Invalid choice! Please try again.")