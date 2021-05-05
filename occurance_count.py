def solution(A):
    dict_ = {}
    list_item = []
    if len(set(A)) == 1:
        return max(A)
    else:

        for i in A:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1

        for k, v in dict_.items():
            if k == v:
                list_item.append(k)
    print(list
    return max(list_item)


print(solution([3, 1, 4, 1, 5]))
