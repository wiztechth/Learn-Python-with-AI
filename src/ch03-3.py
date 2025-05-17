# Strings are sequences of characters enclosed in single, double, or triple quotes
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a 
multi-line string"""

print(single_quotes)
print(double_quotes)
print(triple_quotes)

# String concatenation
greeting = single_quotes + " " + double_quotes + "!"
print(greeting)  # Output: Hello World!

# String repetition
laugh = "ha" * 3
print(laugh)  # Output: hahaha

# String indexing
s = "Python"
print(s[0])    # Output: P (first character)
print(s[-1])   # Output: n (last character)

# String slicing
print(s[1:4])  # Output: yth (characters from index 1 to 3)
print(s[:2])   # Output: Py (first two characters)
print(s[2:])   # Output: thon (from index 2 to end)

# String length
print(len(s))  # Output: 6
print("Length of string:", len(s))  # Output: Length of string: 6


# # Replacing text
# print(text.replace("python", "programming"))  # Output: "  learn programming  "

# # Splitting strings
# words = "apple,banana,cherry".split(",")
# print(words)  # Output: ['apple', 'banana', 'cherry']

# # Joining strings
# fruits = ["apple", "banana", "cherry"]
# print(", ".join(fruits))  # Output: apple, banana, cherry

# # String formatting (f-strings)
# name = "Alice"
# age = 25
# print(f"My name is {name} and I'm {age} years old.")  # Output: My name is Alice and I'm 25 years old.

# # Escape characters
# print("This is a \"quote\"")  # Output: This is a "quote"
# print("Line 1\nLine 2")       # Output: Line 1 (newline) Line 2