import math
import os
import random
import re
import sys

# Complete the countTriplets function below.


def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in arr[::-1]:
        if i*r in dictPairs:
            count += dictPairs[i*r]
        if i*r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        dict[i] = dict.get(i, 0) + 1

    return count


countTriplets([1, 2, 2, 4], 2)
