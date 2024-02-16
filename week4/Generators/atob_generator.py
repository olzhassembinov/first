from math import pow

def squares(a, b):
    x = a
    while x <= b:
        yield pow(x, 2)
        x += 1
    
numbers = squares(int(input('a: ')), int(input('b: ')))

for value in numbers:
    print(value)