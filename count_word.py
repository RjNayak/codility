import re
if __name__ == '__main__':
    sequence = 'ababcabcab'
    word = 'ab'
    index_lst = []
    count_lst = []
    conunt = 0
    chunks = [sequence[i:i+len(word)]
              for i in range(0, len(sequence), len(word))]
    for x in range(0, len(chunks)):
        if chunks[x] == word:
            index_lst.append(x)

    count_lst = [j-i for i, j in zip(index_lst[:-1], index_lst[1:])]

    print(index_lst)
    print(count_lst)
