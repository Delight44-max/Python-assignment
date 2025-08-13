rows = 10

for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()  # move to next line

print()  # blank line between patterns

# Pattern B: Left-aligned decreasing triangle
for i in range(rows, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print()


for i in range(1, rows + 1):
    for space in range(rows - i):
        print(' ', end='')  # leading spaces
    for star in range(i):
        print('*', end='')
    print()

print()

for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(' ', end='')  
    for star in range(i):
        print('*', end='')
    print()