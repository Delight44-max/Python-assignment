def two_D_list(my_list):
    row_sums = []
    for rows in my_list:
        row_sums.append(sum(rows))
    return row_sums


result = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]

print(two_D_list(result))