num1 = input("請輸入被除數:")
num2 = input("請輸入除數:")

def GCD(x, y):

    r = x % y

    if (r == 0):

        return y

    else:
        
        return GCD(y, r)

print("遞迴模式")
print(GCD(eval(num1), eval(num2)))