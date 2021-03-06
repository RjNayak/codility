def LetterChanges(str):
    vowels = 'aeiou'
    for c in str:
        if c == 'z':
            str = str.replace(c, 'a')
        elif c not in vowels:
            str = str.replace(c, chr(ord(c)+1))
        else:
            str = str.replace(c, c.upper())

    return str


if __name__ == '__main__':
    string = input('Enter an input string: ')
    print(LetterChanges(string))
