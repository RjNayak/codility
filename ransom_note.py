#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    result = 'No'
    print(Counter(magazine))
    print(Counter(note))
    # for words in magazine:
    #     _dict.setdefault(words, 0)
    #     _dict[words] += 1
    # for words in note:
    #     if words in _dict:
    #         _dict[words] -= 1
    #     else:
    #         return False
    # if all([x >= 0 for x in _dict.values()]):
    #     result = 'Yes'
    #     print(result)
    # else:
    #     print(result)
    if (Counter(note) - Counter(magazine)) == {}:
        result = 'Yes'
    else:
        result = 'No'
    print(result)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
