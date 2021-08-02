t = [9, 3, 6, 4, 2, 0, 7, 5, 8, 1]

##fuseSort needs a method to fuse 2 sorted lists while sorting them

def fuseIter(T1, T2):
    T, T1c, T2c = [], T1.copy(), T2.copy()
    while T1c != [] and T2c != [] :
        if T1c[0] < T2c[0] :
            T.append(T1c.pop(0))
        else :
            T.append(T2c.pop(0))
    if T1c == [] :
        return T+T2c
    return T+T1c

def fuseRec(T1, T2):
    if T1 == [] :
        return T2
    elif T2 == [] :
        return T1
    if T1[0] < T2[0] :
        return [T1[0]] + fuseRec(T1[1:], T2)
    return [T2[0]] + fuseRec(T1, T2[1:])

#Both these methods are in O(n1+n2) complexity
#with n1 and n2 the lengths of the lists to fuse
#but the recursive one is aweful memory-wise

def fuseSort(T):
    n = len(T)
    if n <= 1 :
        return T
    return fuseIter(fuseSort(T[:n//2]), fuseSort(T[n//2:]))
#O(n*ln(n))


def quickSort(T):
    n = len(T)
    if n <= 1 :
        return T
    T1, T2 = [], []
    for i in range(n) :
        if i != 0 :
            if T[i] <= T[0] :
                T1.append(T[i])
            else :
                T2.append(T[i])
    return quickSort(T1) + [T[0]] + quickSort(T2)
#O(n*ln)
