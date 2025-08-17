def even_numbers(numbers):
    return numbers % 2 == 0


def is_even():
    return list(filter(even_numbers, range(1, 21)))

print(is_even())

    
