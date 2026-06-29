# Q8 - Tuples + Dictionaries + OOP

class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])


# Dictionary
employees = {}

# Add 3 Employees
for i in range(3):
    print(f"\nEnter Details of Employee {i+1}")

    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employees[emp_id] = Employee(emp_id, name, department, salary)

# Display All Employees
print("\n----- Employee Details -----")

for employee in employees.values():
    employee.show_details()