# This is heapsort
# sort() sorts array a in descending order
# sift(p,q) heapifies array a from position p to q
# heap is a max-heap, that is, maximum at the root

import random
from time import time, clock


def out(n):
    for i in range(1, n + 1):
        print(a[i])
    print('\n')


def swap(i, j):  # This swaps a[i] and a[j]
    w = a[i]
    a[i] = a[j]
    a[j] = w


def siftup(p, q):      # This is to heapify a when a[p] is wrong
    y = a[p]  # a[p] is saved to y
    j = p
    k = 2 * p
    while k <= q:
        z = a[k]
        if k < q:
            if z > a[k + 1]:  # Choose the smaller child
                k += 1
                z = a[k]
        if y <= z:
            break
        a[j] = z
        j = k
        k = 2 * j
    a[j] = y               # y settles down at position j


def build_heap(n):
    for i in reversed(range(1, n / 2 + 1)):
        siftup(i, n)


def sort():
    build_heap(n)
    for i in reversed(range(2, n + 1)):
        swap(1, i)  # swap a[1] and a[i]
        siftup(1, i - 1)


# {main program}
n = input('input n ')
a = []
for i in range(0, 10000):
    a += [int(100 * random.random())]
out(n)
t = clock()
sort()
out(n)
print('time ', clock() - t)
n = input('finished ')