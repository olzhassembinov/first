import re

def split_at_uppercase(string):
    # Use regular expression to split the string at uppercase letters
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

# Read the string from the file
with open('week5/Regex/row.txt', 'r') as file:
    input_string = file.read().strip()

# Split the string at uppercase letters
split_parts = split_at_uppercase(input_string)

# Print the result
print("Original string:", input_string)
print("Parts after splitting at uppercase letters:", split_parts)
