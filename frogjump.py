# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(X, Y, D):
    # write your code in Python 3.6
    # x is current position
    # y is desired postition
    # y-x is the distance to cover
    # d is jumping capacity
    # distance to cover / jumping capacity = number of jumps required

    return math.ceil((Y - X)/D)


print(solution(10, 85, 30))
