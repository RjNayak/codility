def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if n % i == 0:
                status = False
    return status


def printPrimeNumbers(lower_limit, higher_limit):
    return ','.join([str(x) for x in range(lower_limit, higher_limit) if is_prime(x)])


if __name__ == '__main__':
    lower_num = int(input('Enter the lower limit: '))
    higher_num = int(input('Enter the higher limit: '))
    print(printPrimeNumbers(lower_num, higher_num))
