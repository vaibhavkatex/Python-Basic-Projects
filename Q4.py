
# Create a class Student with attributes: name, roll_no, and marks_list (a list ofmarks).
class Student:
# Include methods:__init__ to initialize the student.
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

# add_mark(mark) to add a mark to the list (handle invalid marks).
    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks_list.append(mark)
        else:
            print("Invalid Marks! Enter marks between 0 and 100.")

# get_average() to return the average.
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

# display_info() to show all details.
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())


# Main Program
try:
    name = input("Enter Student Name: ")
    roll = int(input("Enter Roll Number: "))

    student = Student(name, roll)

    print("\nEnter 5 Marks:")
    for i in range(5):
        mark = float(input(f"Mark {i+1}: "))
        student.add_mark(mark)

    student.display_info()

except ValueError:
    print("Invalid Input! Please enter numbers only.")