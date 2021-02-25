import string


def print_rangoli(size):
    # your code goes here
    c = '-'
    alphabet = string.ascii_lowercase
    pattern_list = []
    for i in range(size):
        s = c.join(alphabet[i:size])
        pattern_list.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(pattern_list[:0:-1]+pattern_list))


if __name__ == '__main__':
    print_rangoli(3)
