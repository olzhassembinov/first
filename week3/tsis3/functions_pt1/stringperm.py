from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for perm in perms:
        print(''.join(perm))

# Example usage
user_input = input("Enter a string: ")
print("Permutations:")
print_permutations(user_input)
