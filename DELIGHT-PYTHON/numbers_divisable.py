def get_numbers(number):
    return number % 3 == 0 and number % 5 == 0


def get_divisable_numbers():
    return list(filter(get_numbers, range(1, 51)))


print(get_divisable_numbers())
    