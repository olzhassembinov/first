from math import pow

def generate_number(limit):
    n = 1
    i = 1
    while i < limit:
        yield i
        n += 1
        i = pow(n, 2)

n = int(input())

for value in generate_number(n):
    print(value)