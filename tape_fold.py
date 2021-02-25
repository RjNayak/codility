# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    fold_diff_lis = []
    for x in range(1, len(A)):
        print(A[:x])
        print(A[x:])
        fold_diff_lis.append(abs(sum(A[:x])-sum(A[x:])))

    return min(fold_diff_lis)


print(solution([3, 1, 2, 4, 3]))
