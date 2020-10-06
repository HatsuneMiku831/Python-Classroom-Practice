row = 0
x = 1
u = 1
col = 0

D = {''}
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[row][len(a) % 2] = 1
col = len(a) % 2
y = str(row) + str(col)
D.add(y)

for r in range(len(a) **2 + 1):

    if r <= 1 :

        a[row][len(a) % 2] = 1
        col = len(a) % 2
        y = str(row) + str(col)
        D.add(y)
        #print(r)

    else: 

        if row - 1 < 0 or col + 1 > 2:

            c = (row - 1) % 3
            d = (col + 1) % 3
            y = str(c) + str(d)
            boolean = y in D

            if boolean == True:

                a[row + u][col] = r
                o = row + u

                if u == 2:

                    u = 0

                q = col
                y=str(o)+str(q)
                D.add(y)
                row=o
                col=q

            else:

                  c = (row - 1) % 3
                  d = (col + 1) % 3
                  a[c][d] = r
                  y = str(c) + str(d)
                  D.add(y)
                  row = c
                  col = d 
        else:

            g = row - 1
            d = col + 1
            y = str(g) + str(d)
            boolean = y in D

            if boolean == True:

                a[row + x][col] = r
                h = row + x

                if h == 2:
                    x = 0

                q = col
                y = str(h) + str(q)
                D.add(y)
                row = h
                col = q

            else:

                g = row - 1
                d = col + 1
                a[g][d] = r
                y = str(g) + str(d)
                D.add(y)
                row = g
                col = d

for i in range(len(a)):

    print(a[i])