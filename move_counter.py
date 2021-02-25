#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'countMoves' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countMoves(numbers):
    # Write your code here
    # check if all the elements are same then return 0
    # loop throught he list
    # find the value which is duplicate at set the index to be exempted from increment
    # increase each elemnt by 1
    # increase the counter
    # check if all the lements are same
    # return

    _movement_counter = 1
    i = 0
    if len(set(numbers)) == 1:
        return 0

    while len(set(numbers)) != 1:
        max_value = max(numbers)
        if numbers[i] < max_value:
            numbers[i] += 1
            _movement_counter += 1

        if i < len(numbers)-1:
            i += 1
        else:
            i = 0

    return _movement_counter


if __name__ == '__main__':

    print(countMoves([1, 2, 3]))
