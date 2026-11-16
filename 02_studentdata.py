
# Lab Exercise 2: Student Data Manager Using Files

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add a new student record")
    print("2. Display all student records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Get student details
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        # Store student details in file
        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")

        print("Student record added successfully!")

    elif choice == "2":
        # Display all student records
        try:
            with open("students.txt", "r") as file:
                print("\n===== STUDENT RECORDS =====")

                records = file.readlines()

                if len(records) == 0:
                    print("No student records found.")
                else:
                    for record in records:
                        roll, name, marks = record.strip().split(",")
                        print("Roll Number:", roll)
                        print("Student Name:", name)
                        print("Marks:", marks)
                        print("------------------------")

        except FileNotFoundError:
            print("No student records found. File does not exist.")

    elif choice == "3":
        print("Exiting Student Data Manager. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")