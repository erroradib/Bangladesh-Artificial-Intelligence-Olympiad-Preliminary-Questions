# Adnan Adib

import math

def logis_func(scr):
    return 1 / (1 + math.exp(-scr))


T = int(input())

for x in range(T):

    N = int(input())
    

    scores = list(map(float, input().split()))
    
    for scr in scores:
        probability = logis_func(scr)
        print("{:.9f}".format(probability))

