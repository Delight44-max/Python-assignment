rows = 10

for i in range(1, rows + 1):
    
    for j in range(i):
        print('*', end='')
    
    print('   ', end='') 

    
    for j in range(rows - i + 1):
        print('*', end='')
    
    print('   ', end='')

    for j in range(rows - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    
    print('   ', end='')

    # Pattern D: Right-aligned decreasing triangle
    for j in range(i - 1):
        print(' ', end='')
    for j in range(rows - i + 1):
        print('*', end='')

    print()