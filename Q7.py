# Q7 - Lambda + range() + Lists + Exception Handling

try:
    # Lambda function to calculate square
    square = lambda x: x * x

    # Store squares of numbers 1 to 20
    squares = []

    for i in range(1, 21):
        squares.append(square(i))

    print("All Squares:")
    print(squares)

    print("\nEven Squares:")
    for num in squares:
        if num % 2 == 0:
            print(num)

except Exception as e:
    print("Error:", e)