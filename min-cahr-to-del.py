def solution(S):
    # write your code in Python 3.6
    # find each letter and its repeatation number
    # find the order and fidn the number of letter to be deleted
    char_dict = {}
    result = 0
    dict_list = []
    for i in range(len(S)):
        char_dict[S[i]] = char_dict.get(S[i], 0)+1

    for it in char_dict:
        dict_list.append(char_dict[it])

    dict_list = sorted(dict_list)

    while (len(dict_list) > 0):
        freq = dict_list[-1]
        del dict_list[-1]
        if len(dict_list) == 0:
            return result
        if (freq == dict_list[-1]):
            if (freq > 1):
                dict_list.append(freq-1)
            result += 1
        dict_list = sorted(dict_list)

    return result


print(solution('ccaaffddecee'))
