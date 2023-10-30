#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_and_max = [0, 0]
    current_min = scores[0]
    current_max = scores[0]

    for i in range(1, len(scores)):
        if scores[i] > current_max:
            current_max = scores[i]
            min_and_max[0] += 1
        elif scores[i] < current_min:
            current_min = scores[i]
            min_and_max[1] += 1

    return min_and_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
