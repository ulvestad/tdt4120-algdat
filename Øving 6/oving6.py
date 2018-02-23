from sys import stdin
def sorter(A):
    if len(A)<20:
       return insertion(A)
    else:
        return merge(A)

def insertion(A):
    for index in xrange(1,len(A)):
        value= A[index]
        pos = index
        while pos>0 and A[pos-1]>value:
            A[pos] = A[pos-1]
            pos= pos-1
        A[pos] = value
    return A

def merge(A):
    if len(A)<2:
        return A
    result =[]
    mid = int(len(A)/2)
    left = merge(A[:mid])
    right = merge(A[mid:])
    i = 0
    j =0
    while len(left)> i and len(right)> j:
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result += left[i:]
    result += right[j:]
    return result

def finn(A, nedre, ovre):
    minMaks = []
    t = 0
    
    if nedre < A[0]:
        minMaks.append(A[0])
    elif nedre > A[len(A) - 1]:
        minMaks.append(A[len(A) - 1])
    else:
        for i in range(len(A)):
            if nedre < A[i]:
                minMaks.append(A[i - 1])
                break
            elif nedre == A[i]:
                minMaks.append(A[i])
                break
            t += 1
    
    if ovre < A[0]:
        minMaks.append(A[0])
    elif ovre > A[len(A) - 1]:
        minMaks.append(A[len(A) - 1])
    else:
        for i in range(t, len(A)):
            if ovre <= A[i]:
                minMaks.append(A[i])
                break
    
    return minMaks
    

def init():
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x))

    sortert = sorter(liste)
    
    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])
init()
