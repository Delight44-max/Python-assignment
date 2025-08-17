def tuple_to_list(main_tuple, index, new_value):

    my_tuple = main_tuple
    changed = list(my_tuple)
    changed[index] = new_value
    new_tuple = tuple(changed)
    return new_tuple


my_tuple = ("apple", "banana", "cherry")

result = tuple_to_list(my_tuple, 1, "mango")

print(result)

