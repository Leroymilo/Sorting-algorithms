"""
Implementing the radix sort algorithm with the counting sort
https://www.youtube.com/watch?v=XiuSW_mEn7g
"""

import numpy as np
import CountingSort as CS

def radixSort(L) :
    'L is a list of integers to sort'
    assert type(L) is list
    for element in L :
        assert type(element) is int

    newL = np.array([str(n) for n in L], dtype = str)
    lengths = np.array([len(element) for element in newL], dtype = int)
    maxLen = int(np.max(lengths))

    for k in range(len(newL)) :
        while len(newL[k]) < maxLen :
            newL[k] = '0' + newL[k]

    for k in range(1, maxLen+1) :
        newL = CS.countSort(newL, i = maxLen-k)

    return [int(newL[k]) for k in range(len(L))]
