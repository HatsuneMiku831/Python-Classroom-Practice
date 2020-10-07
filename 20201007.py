def fattor(n):

    if (n != 1):

        return n * fattor(n - 1)

    else:
        
        return 1

print(fattor(1))