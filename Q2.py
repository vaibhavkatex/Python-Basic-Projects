# Q2. Strings + Loops + Functions)
# Write a function analyze_string(s) that takes a string as input and:
# Prints its length using len().
# Prints the string in reverse using slicing.
# Counts and prints how many vowels (a,e,i,o,u) are in the string (caseinsensitive).
# Uses a for loop with range() to print each character with its positive andnegative index.
# Call this function with user input and handle empty string case.


def analyze_string(s):
    # Prints its length using len().
    print("Length:", len(s))

    # Prints the string in reverse using slicing.   
    print("Reverse:", s[::-1])

    # Counts and prints how many vowels (a,e,i,o,u) are in the string (caseinsensitive).
    vowels = "aeiou"
    count = 0


    # Uses a for loop with range() to print each character with its positive andnegative index.
    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Vowels:", count)

    print("\nCharacters with Index:")
    for i in range(len(s)):
        print(i, s[i], i - len(s))


text = input("Enter a string: ")

# handle empty string case.
if text == "":
    print("String is empty!")
else:
    analyze_string(text)