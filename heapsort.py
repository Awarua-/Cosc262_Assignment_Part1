# This is heapsort
# sort() sorts array a in descending order
# sift(p,q) heapifies array a from position p to q
# heap is a max-heap, that is, maximum at the root

import random
from time import time, clock

c = 0

def out(n, a):
    for i in range(1, n + 1):
        print(a[i])
    print('\n')


def swap(i, j, a):  # This swaps a[i] and a[j]
    w = a[i]
    a[i] = a[j]
    a[j] = w


def siftup(p, q, a):      # This is to heapify a when a[p] is wrong
    global c
    y = a[p]  # a[p] is saved to y
    j = p
    k = 2 * p
    isHeap = False
    while k <= q and not isHeap:
        z = a[k]
        if k < q:
            c += 1
            if z < a[k + 1]:  # Choose the smaller child
                k += 1
                z = a[k]
        c += 1
        if y >= z:
            isHeap = True
        else:
            a[j] = z
            j = k
            k = 2 * j
    a[j] = y               # y settles down at position j


def build_heap(n, a):
    for i in reversed(range(1, int(n / 2 + 1))):
        siftup(i, n, a)


def sort(n, a):
    build_heap(n, a)
    for i in reversed(range(2, n + 1)):
        swap(1, i, a)  # swap a[1] and a[i]
        siftup(1, i - 1, a)


# {main program}
def main(n, a):
    # out(n)
    print(a)
    b = c
    t = clock()
    sort(n, a)
    # out(n)

    print(a)
    print(b)
    print(c)
    print('time ', clock()-t, 'c =', c - b)

# main(10, [88, 50, 23, 61, 85, 20, 86, 49, 66, 33, 3])
# main(10, [88, 50, 23, 61, 85, 20, 86, 49, 66, 33, 3])

