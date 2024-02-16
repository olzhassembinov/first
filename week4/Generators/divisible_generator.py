def divisible_generator(n):
    a = 0
    while a < n:
        if a % 3 == 0 and a % 4 == 0:
            yield a
        a += 1

numbers = divisible_generator(int(input()))

for value in numbers:
    print(value)