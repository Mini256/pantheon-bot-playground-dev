def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

def truncate(s, max_len):
    # BUG: no check for max_len <= 0
    if len(s) > max_len:
        return s[:max_len] + "..."
    return s

def is_palindrome(s):
    # BUG: case-sensitive, "Racecar" would fail
    return s == s[::-1]
