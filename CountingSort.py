"""
Implementing the counting sort algorithm
https://www.youtube.com/watch?v=OKd534EWcdk
"""

import numpy as np
    
def countSort(L, i=0):
    'L is the array of strings to sort, i (integer) is the rank at which L is sorted'
    """
    example : countSort(np.array(['201', '023', '001', '123', '642']), 2)
    will return : ['201' '001' '642' '023' '123'] (np.ndarray)
    """
    assert type(L) is np.ndarray and type(i) is int
    for element in (L) :
        assert type(element) is np.str_ and len(element) > i
    
    m = np.max( np.array( [int(L[k][i]) for k in range(len(L))], dtype = int) )
    startInd = np.zeros(m+1, dtype = int)
    
    for element in L :
        for number in range(m+1) :
            if int(element[i]) == number :
                startInd[number] += 1

    for number in range(1, m+1) :
        startInd[number] += startInd[number-1]

    for number in range(1, m+1) :
        startInd[-number] = startInd[-number-1]
    startInd[0] = 0
    
    newL = ['' for k in range(len(L))]
    for element in L :
        for number in range(m+1) :
            if int(element[i]) == number :
                newL[startInd[number]] = element
                startInd[number] += 1
                
    return np.array(newL)
