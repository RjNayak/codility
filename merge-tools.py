def merge_the_tools(string, k):

    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
