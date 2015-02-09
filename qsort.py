#
# quicksort
#

# make a list for sorting
from random import randint
size = 20
L = [ randint(0,size * 2) for i in range(size)]

def qsort(L):
    if (len(L) > 1):
        last = len(L) - 1
        swap(L,int(len(L)/2),last)
        pivot = L[last]
        high = 0
        for i in range(len(L)):
            if L[i] < pivot:
                swap(L,i,high)
                high += 1
        swap(L,high,last)
        L[:high] = qsort(L[:high])
        L[high+1:] = qsort(L[high+1:])
    return L

def swap(L,i,j):
    if i != j:
        tmp = L[i]
        L[i] = L[j]
        L[j] = tmp

print("raw:   ", L)
print("sorted:", qsort(L))
