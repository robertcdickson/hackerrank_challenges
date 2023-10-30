#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    mode_bird_ids = []
    max_count = max([arr.count(x) for x in set(arr)])
    for bird_id in set(arr):
        bird_id_count = arr.count(bird_id)
        if bird_id_count == max_count:
            mode_bird_ids.append(bird_id)

    return min(mode_bird_ids)

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
