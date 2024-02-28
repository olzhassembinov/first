import re

with open("week5/Regex/row.txt", "r") as file:
    y = file.read()

x = re.findall("[A-Z][a-z]+", y)
print(x)

file.close()