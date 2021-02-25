#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Write your code here
    result = 0
    for i in range(0, len(order)):
        print(sum(order[0:i]))
        if sum(order[0:i]) <= k and sum(order[0:i]) != 0:
            result = i+1
    return result


if __name__ == "__main__":
    print(filledOrders([4, 5, 6], 3))
