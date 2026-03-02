"""Simple calculator module with intentional bugs for review testing."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # BUG: no zero division check
    return a / b


def power(base, exp):
    result = 1
    for _ in range(exp):  # BUG: doesn't handle negative exponents
        result *= base
    return result


def average(numbers):
    # BUG: no empty list check
    return sum(numbers) / len(numbers)
