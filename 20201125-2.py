finnum = []

def testOwO(num):

    sumnum = [1, 1]

    for i in range(2, num + 1):

        sumnum.append(sumnum[i - 1] + sumnum[i - 2])

    return sumnum

print("f( n ) = f( n - 1 ) + f( n - 2 )")

num1 = eval(input("n? "))

finnum = testOwO(num1)

finnum.pop(0)

#print(finnum)
print("f(", num1, ") =", finnum[num1 - 1])