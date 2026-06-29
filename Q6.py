# Q6 - Sets + Tuples + Modules

import random
import math

try:
    numbers = set()

    print("Enter 10 Numbers:")

    for i in range(10):
        num = int(input(f"Number {i+1}: "))
        numbers.add(num)

    print("\nUnique Numbers (Set):", numbers)

    num_tuple = tuple(numbers)
    print("Tuple:", num_tuple)

    if len(num_tuple) >= 3:
        print("3 Random Numbers:", random.sample(num_tuple, 3))
    else:
        print("Not enough unique numbers to pick 3.")

    total = sum(num_tuple)
    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Invalid Input! Please enter numbers only.")

except Exception as e:
    print("Error:", e)