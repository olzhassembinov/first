import re

with open("week5/Regex/row.txt", "r") as file:
    y = file.read()

x = re.findall("ab{2, 3}", y)
print(x)

file.close()