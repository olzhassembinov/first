import re

# Read the text file
with open('week5/Regex/row.txt', 'r') as file:
    text = file.read()

# Define the pattern
pattern = r'[ ,.]'

# Replace all occurrences of space, comma, or dot with a colon
result = re.sub(pattern, ':', text)

# Print the result
print("Original text:")
print(text)
print("\nText after replacement:")
print(result)
