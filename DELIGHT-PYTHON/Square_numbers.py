def get_squares(numbers):
    return numbers**2




def squares():
    return list(map(get_squares, range(1, 11)))


print(squares())