def is_palindrome(s):
    # Standardize input by cleaning casing
    cleaned_s = s.lower()
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("Radar"))  # Output: True
print(is_palindrome("python")) # Output: False