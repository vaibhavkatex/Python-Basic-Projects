# Q9 - Strings + Sets + Exception Handling + Modules

import math

try:
    sentence = input("Enter a sentence: ")

    # Convert sentence into words
    words = sentence.split()

    # Store unique words in a set
    unique_words = set(words)

    # Print unique words in sorted order
    print("\nUnique Words:")
    for word in sorted(unique_words):
        print(word)

    # Total unique words raised to power 2
    total = len(unique_words)
    print("\nTotal Unique Words:", total)
    print("Power of 2:", math.pow(total, 2))

except Exception as e:
    print("Error:", e)