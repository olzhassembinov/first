def reverse_generator(n):
    a = n
    while a > 0:
        yield a
        a -= 1
    
numbers = reverse_generator(int(input()))

for value in numbers:
    print(value)