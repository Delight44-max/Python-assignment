def keep_tuples(lists):
    return lists[0] > 2


my_list = [(1,"A"), (4, "B"), (2, "C")]

print(tuple(filter( keep_tuples, my_list)))