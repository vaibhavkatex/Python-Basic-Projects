# Create a function manage_marks() that:
# Stores them in a list.
def manage_marks():
    marks = []

# Takes 5 subject marks as input from the user.
    try:
        print("Enter marks of 5 subjects:")

        for i in range(5):
            mark = float(input(f"Subject {i+1}: "))
            marks.append(mark)

        average = sum(marks) / len(marks)

# Calculates and prints the average, highest, and lowest marks.
        print("\nMarks List:", marks)
        print("Average Marks:", average)
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))

# Sorts the list in descending order and prints it.
        marks.sort(reverse=True)
        print("Marks in Descending Order:", marks)

# Handles ValueError if non-numeric input is given.
    except ValueError:
        print("Invalid Input! Please enter only numbers.")


# Function Call
manage_marks()