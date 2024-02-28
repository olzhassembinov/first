import re

def camel_to_snake(string):
    # Use regular expression to convert camel case to snake case
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return snake_case

# Read the string from the file
file_path = 'week5/Regex/row.txt'  # Update the file path accordingly
with open(file_path, 'r') as file:
    input_string = file.read().strip()

# Convert camel case to snake case
snake_case_string = camel_to_snake(input_string)

# Print the result
print("Original camel case string:", input_string)
print("Converted snake case string:", snake_case_string)
