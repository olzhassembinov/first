import re

def snake_to_camel(snake_case):
    # Split the snake case string by underscore
    words = snake_case.split('_')
    # Capitalize the first letter of each word except the first one
    camel_case = ''.join([words[0]] + [word.capitalize() for word in words[1:]])
    return camel_case

# Read the snake case string from the file
with open('week5/Regex/row.txt', 'r') as file:
    snake_case_string = file.read().strip()

# Convert snake case to camel case
camel_case_string = snake_to_camel(snake_case_string)

# Print the result
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)
