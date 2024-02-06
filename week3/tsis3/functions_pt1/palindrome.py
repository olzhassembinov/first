def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example Usage
word = "madam"
result = is_palindrome(word)

if result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
