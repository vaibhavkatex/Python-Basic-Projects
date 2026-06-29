# Write a function student_database() that uses a dictionary (roll number as key) tostore student records.
def student_database():
    students = {}

# Provide a menu using while loop:Add student (name, age, city)Search student by roll number
    while True:
        print("\n----- Student Database -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student Added Successfully!")

            except ValueError:
                print("Invalid Input!")

        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number to Search: "))
                student = students.get(roll)

                if student:
                    print(student)
                else:
                    print("Student Not Found!")

            except ValueError:
                print("Invalid Roll Number!")

# Display all students
        elif choice == "3":
            if len(students) == 0:
                print("No Student Records Found!")
            else:
                for roll, data in students.items():
                    print("\nRoll No:", roll)
                    print("Name:", data["Name"])
                    print("Age:", data["Age"])
                    print("City:", data["City"])

# ExitUse get(), update(), and proper exception handling for invalid inputs
        elif choice == "4":
            print("Program Ended.")
            break

        else:
            print("Invalid Choice!")


# Function Call
student_database()