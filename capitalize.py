def solve(s):
    words = str(s).split(' ')
    result = []
    for word in words:
        s = s.replace(word, word.capitalize())

    print(s)


solve('1 w 2 r 3g')
