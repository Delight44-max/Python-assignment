import math

def divide(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Invalid input: must be a number")

    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5