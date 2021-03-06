def factorail(n):
    if n == 0:
        return 1
    else:
        return n * factorail(n-1)


n = int(input('Input a number to compute '))
print(factorail(n))
