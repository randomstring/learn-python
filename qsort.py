#
# quicksort
#

# make a list for sorting
from random import randint
size = 20
L = [ randint(0,size * 2) for i in range(size)]

#
# first try
#
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

#
# In place qsort
# 
def qsort2(L, start, end):
    # print("qsort2(", start, end, L,")")
    length = end - start + 1
    if (length > 1):
        swap(L,start + int(length/2),end)
        pivot = L[end]
        high = start
        for i in range(start,end+1):
            if L[i] < pivot:
                swap(L,i,high)
                high += 1
        swap(L,high,end)
        qsort2(L,start, high - 1)
        qsort2(L,high+1, end)

def swap(L,i,j):
    if i != j:
        tmp = L[i]
        L[i] = L[j]
        L[j] = tmp

print("raw:   ", L)
print("sorted:", qsort(L))

L = [ randint(0,size * 2) for i in range(size)]
print("raw:   ", L)
qsort2(L,0,len(L)-1)
print("sorted:", L)
