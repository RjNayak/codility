
def solution(A):

    sum_list = []

    for i in A:
        for j in A:
            if i != j:
                sum_list.append(i+j)

    print(list(set(sum_list)))


solution([51, 71, 17, 42])
