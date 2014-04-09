# This is heapsort
# sort() sorts array a in descending order
# sift(p,q) heapifies array a from position p to q
# heap is a max-heap, that is, maximum at the root
from time import clock

c = 0


def swap(i, j, a):  # This swaps a[i] and a[j]
    w = a[i]
    a[i] = a[j]
    a[j] = w


def siftup(p, q, a):      # This is to heapify a when a[p] is wrong
    global c
    y = a[p]  # a[p] is saved to y
    j = p
    k = 2 * p
    isheap = False
    while k <= q and not isheap:
        z = a[k]
        if k < q:
            c += 1
            if z < a[k + 1]:  # Choose the smaller child
                k += 1
                z = a[k]
        c += 1
        if y >= z:
            isheap = True
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
    b = c
    t = clock()
    sort(n, a)
    assert a[1:] == sorted(a[1:]), "List not sorted, error!!!!!!!!!!"
    t = clock() - t
    return t, c - b