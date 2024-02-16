import math

sides = int(input('Input number of sides: '))
side_length = int(input('Input the length of a side: '))
area = int(sides / 4 * math.pow(side_length, 2) * 1 / math.tan(math.pi/sides))

print(f"The area of polygon is:{area}")