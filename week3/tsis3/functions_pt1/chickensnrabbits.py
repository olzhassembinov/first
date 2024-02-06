def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r
    return None

# Test the function with the given problem
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)