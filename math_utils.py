def divide(a, b):
    # BUG: no zero check
    return a / b

def average(nums):
    # BUG: crashes on empty list
    return sum(nums) / len(nums)

def power(base, exp):
    return base ** exp
