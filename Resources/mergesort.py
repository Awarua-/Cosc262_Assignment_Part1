# This is mergesort
# mergesort(p,q) sorts array a from position p to q

import random
from time import time, clock


c = 0


def out(n):
    for i in range(1, n+1):
        print(a[i])
    print('\n')


def mergesort(p, q):
    if p < q:
        m = (p + q) / 2
        mergesort(p, m)
        mergesort(m + 1, q)
        merge(p, m + 1, q + 1)

# merge(p,m,q) merges array a from position p to m
# and position m+1 to q


def merge(p, r, q):
    global c   # c is comparison counter
    i = p
    j = r
    k = p
    while i < r and j < q:
        c += 1
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    while i < r:
        b[k] = a[i]
        i += 1
        k += 1
   
    while j < q:
        b[k] = a[j]
        j += 1
        k += 1
    for k in range(p, q):
        a[k] = b[k]


#{ main program }
n = input('input n ')
a = []
for i in range(0, 20000):
    a += [int(100 * random.random())]
b = []
for i in range(0, 20000):
    b += [0]
#out(n)
t = clock()
mergesort(1, n)
#out(n)
print('time ', clock() - t, 'c=', c)
n = input('finished ')