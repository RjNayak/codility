#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Write your code here
    # parent=[-1,0,0,1,1,2]
    #       [1,2,2,1,1,1]
    # file_size=[1,4,3,4]
    root = []
    branches = []
    for i in range(0, len(parent)):
        if parent[i] == -1:
            root = i
        if parent[i] == root:
            branches.append(i)

    print(branches)


if __name__ == '__main__':
    mostBalancedPartition([-1, 0, 0, 1, 1, 2], [1, 2, 2, 1, 1, 1])
    # print(result)
