num1 = input("請輸入被除數:")
num2 = input("請輸入除數:")

wx = eval(num1)
wy = eval(num2)

def GCD(x, y):

    r = x % y

    if (r == 0):

        return y

    else:
        
        return GCD(y, r)

print("遞迴模式")
print(GCD(eval(num1), eval(num2)))

wr = wx % wy

while (wr != 0):

    wx = wy
    wy = wr

    wr = wx % wy

print("迴圈模式")
print(wy)