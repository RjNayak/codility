import re
if __name__ == "__main__":
    for _ in range(int(input())):
        u = input()

        try:
            assert re.search(r'.*[A-Z].*[A-Z].*', u)
            assert re.search(r'.*[0-9].*[0-9].*[0-9].*', u)
            assert re.search(r'[A-Za-z0-9]{10}', u)
            assert not re.search(r'.*(.).*\1.*', u)
            assert len(u) == 10
        except:
            print('Invalid')
        else:
            print('Valid')
