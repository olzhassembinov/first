def even_generator(n):
    a = 0
    while a < n:
        yield a
        a += 2

evens = even_generator(int(input()))
numbers = []
for value in evens:
    numbers.append(value)

print(numbers)