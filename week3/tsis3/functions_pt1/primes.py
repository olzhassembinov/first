def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Test the function
numbers_list = [2, 3, 5, 8, 13, 21, 7, 11]
result = filter_prime(numbers_list)

print("Original list:", numbers_list)
print("Prime numbers:", result)
