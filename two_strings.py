
import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    result = 'No'
    for c in s1:
        if c in s2:
            result = 'Yes'
    # print(set(s1))
    # print(set(s1))
    print(result)
    # return 'YES' if set(s1) & set(s2) else 'NO'


if __name__ == '__main__':
    twoStrings('hello', 'world')
