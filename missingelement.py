# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # find the min and max of the list
    # find the total sum of the values from min to max
    # find the sum of elements currently in the lsit
    # return the difference
    total_sum_shouldbe = sum(range(min(A), max(A))+1)
    current_total_sum = sum(A)

    return total_sum_shouldbe - current_total_sum


print(solution([2, 3, 1, 5]))
