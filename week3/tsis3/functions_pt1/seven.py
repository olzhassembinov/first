def spy_game(nums):
    # Initialize variables to track the presence of 0, 0, and 7
    has_0 = False
    has_00 = False

    for num in nums:
        # Check for the sequence 0, 0, 7
        if num == 0 and has_0:
            has_00 = True
        elif num == 0:
            has_0 = True
        elif num == 7 and has_00:
            return True

    return False

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False
