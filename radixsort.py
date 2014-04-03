__author__ = 'Dion'

import copy
from time import clock


alpha_rep = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20,
             'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31,
             'w': 32, 'x': 33, 'y': 34, 'z': 35}


def main(a, base, max_num_len):
    buckets = []
    if base == 1:
        buckets.append([])
        buckets.append([])
    else:
        for i in range(0, base):
            buckets.append([])

    t = clock()

    i = max_num_len - 1
    while i >= 0:
        for k in a[1:]:
            m = copy.deepcopy(k)
            m = list(m)
            x = m[i]
            try:
                int(x)
                buckets[int(m[i])].append(k)
            except ValueError:
                buckets[alpha_rep[x]].append(k)

        a = a[:1]
        for j in buckets:
            r, j[:] = j[:], []
            a.extend(r)

        i -= 1

    print('time ', clock() - t)