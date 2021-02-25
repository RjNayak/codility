# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # [-1,1,3,3,3,2,3,2,1,0]
    diff = [{A.index(i), A.index(j)} for i, j in zip(A[:-1], A[1:])]
    for t in diff:
        print(t)


solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0])
