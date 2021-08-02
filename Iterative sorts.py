t = [9, 3, 6, 4, 2, 0, 7, 5, 8, 1] #Test list

def selectSort(T):
    n = len(T)
    for i in range(n-1) :
        iMin = i
        for j in range(i+1,n) :
            if T[j]<T[iMin] :
                iMin = j
        if iMin != i :
            T[i], T[iMin] = T[iMin], T[i]
    return None
#O(n²)


def bubleSort(T):
    n = len(T)
    for i in range(n-1) :
        for j in range(n-i-1) :
            if T[j] > T[j+1] :
                T[j+1], T[j] = T[j], T[j+1]
    return None
#O(n²)

def insertSort(T):
    n = len(T)
    for i in range(n) :
        j = i
        key = T[j]
        while j > 0 and T[j-1] > key :
            T[j] = T[j-1]
            j = j-1
        T[j] = key
    return None
#O(n²)






