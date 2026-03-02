def divide(a, b):
    # BUG: no zero check
    return a / b

def average(nums):
    # BUG: crashes on empty list
    return sum(nums) / len(nums)

def power(base, exp):
    return base ** exp

def clamp(value, min_val, max_val):
    # BUG: no validation that min_val < max_val
    return max(min_val, min(max_val, value))
