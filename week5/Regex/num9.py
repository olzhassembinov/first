import re

def insert_spaces(string):
    # Use regular expression to insert spaces before capital letters
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return modified_string

# Read the string from the file
file_path = 'week5/Regex/row.txt'  # Update the file path accordingly
with open(file_path, 'r') as file:
    input_string = file.read().strip()

# Insert spaces between words starting with capital letters
modified_string = insert_spaces(input_string)

# Print the result
print("Original string:", input_string)
print("String with spaces inserted between words starting with capital letters:")
print(modified_string)
