def solution(S):
    num_list = []
    if len(S) <= 2:
        return int(S)

    for i in range(0, len(S)-1):
        num_list.append(int(S[i]+S[i+1]))
    return max(set(num_list))


print(solution('10101'))
