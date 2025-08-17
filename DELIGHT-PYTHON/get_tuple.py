def change_tuple_item(tup, index, new_value):
    tup[1][index] = new_value

    return tup


tup = (1, [99, 4], 5)
print(change_tuple_item(tup, 1, 99))