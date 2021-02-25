# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    N = "{0:b}".format(N)
    gaps = []
    lst = []
    for i in range(len(N)):
        if (N[i] == '1'):
            lst.append(i)

    if lst.count('1') < 2:
        return 0
    else:
        for x in range(0, len(lst)-1):
            gaps.append(abs(lst[x]-lst[x+1])-1)
        return max(gaps)

    print(max(gaps))


solution(32)
