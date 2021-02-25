def solution(N):
    # write your code in Python 3.6
    new_str_value = list(str(N))
    result = []
    for x in new_str_value:
        print(x)
        if int(x) < 5:
            result.append(5)
            result.append(''.join(new_str_value[new_str_value.index(x):]))
            break
        else:
            result.append(x)
    return ''.join(str(i) for i in result)


solution(268)
