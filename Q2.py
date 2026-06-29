
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