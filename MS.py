row = 0

square = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

col = int(len(square) / 2)
square[row][col] = 1

for i in range(2, len(square) ** 2 + 1):

    rown = (row - 1) % 5
    coln = (col + 1) % 5

    if square[rown][coln] == 0:

        rown = (row - 1) % 5
        coln = (col + 1) % 5
        square[rown][coln] = i
        row = rown
        col = coln

    else:
        
        square[row + 1][col] = i
        row = row + 1

for n in range(len(square)):

    print(square[n])