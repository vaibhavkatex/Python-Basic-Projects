# Q3 - Lists + Functions + Exception Handling

def manage_marks():
    marks = []

    try:
        print("Enter marks of 5 subjects:")

        for i in range(5):
            mark = float(input(f"Subject {i+1}: "))
            marks.append(mark)

        average = sum(marks) / len(marks)

        print("\nMarks List:", marks)
        print("Average Marks:", average)
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))

        marks.sort(reverse=True)
        print("Marks in Descending Order:", marks)

    except ValueError:
        print("Invalid Input! Please enter only numbers.")


# Function Call
manage_marks()