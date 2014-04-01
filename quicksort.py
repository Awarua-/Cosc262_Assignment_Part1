# This is quicksort
# sort(left,right) sorts array a from position left to right
# partition(left,right) partitions array a from position left to right
# with pivot x=a[left], and returns m such that after partition
# a[left .. m-1] <= x=a[m] <= a[m+1 .. right]

import random
from time import time, clock
c = 0

def out(n, a):
    for i in range(1, n+1):
        print(a[i])
    print('\n')


def sort(left, right, a):
    if left < right:
        m = partition(left, right, a)
        sort(left, m - 1, a)
        sort(m + 1, right, a)


def partition(left, right, a):      # x is the pivot
    global c
    x = a[left]
    i = left
    j = right + 1  # i goes right, j goes left

    while i < j:
        j -= 1

        if i == j:
            break

        while a[j] >= x:          # while a[j]>=x,
            c += 1
            j -= 1                # j goes left
            if i == j:
                break
        c += 1

        if i == j:
            break
        a[i] = a[j]
        i += 1
        if i == j:
            break

        while a[i] <= x:          # while a[i]<=x,
            c += 1
            i += 1                # i goes right
            if i == j:
                break
        c += 1
        if i == j:
            break

        a[j] = a[i]               # a[i] is copied to a[j]
    a[i] = x                    # pivot x settles down at i
    return i

def main(n, a):
    print(a)
    b = c
    # {main program}
    t = clock()
    sort(1, n, a)
    print(a)
    print(b)
    print(c)
    print('time ', clock()-t, 'c =', c - b)