def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    if number_one == 0 or number_two == 0:
        raise ZeroDivisionError('You cant divide by zero!')
    return number_one / number_two

def is_even(n):
    """Return True if n is an even number, else False."""
    return n % 2 == 0