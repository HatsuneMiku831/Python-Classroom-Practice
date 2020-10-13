row = 0

a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

col = int(len(a) / 2)
a[row][col] = 1

for i in range(2, len(a) ** 2 + 1):

    row_next = (row - 1) % 5
    col_next = (col + 1) % 5

    if a[row_next][col_next] == 0:

        row_next = (row - 1) % 5
        col_next = (col + 1) % 5
        a[row_next][col_next] = i
        row = row_next
        col = col_next

    else:
        
        a[row + 1][col] = i
        row = row + 1

for s in range(len(a)):

    print(a[s])