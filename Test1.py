sum = 1

for r in range(1, 9999):

    sum = sum / r

    if sum < 10 ** -7:

        break

n = r

sum = 1

total = 1

for i in range(1, n + 1):

   sum = sum / i
   total = total + sum

y = float(total)

print("e = %.7f"%y)