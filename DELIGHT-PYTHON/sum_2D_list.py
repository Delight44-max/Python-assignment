def rows(my_lists):
    row_sum = []
    
    for row in my_lists:
        total = 0
        for elements in row:
            total += elements
        row_sum.append(total)
    return row_sum



result = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(rows(result))
    
