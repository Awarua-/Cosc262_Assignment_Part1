__author__ = 'Dion'


def main(a, base, max_len):
    buckets = []
    for i in range(0, base):
        buckets.append([])

    i = 0
    while i < max_len:
        for k in a[1:]:
            x = (k // base ** i) % base
            buckets[x].append(k)

        a = a[:1]
        for j in buckets:
            r, j[:] = j[:], []
            a.extend(r)

        i += 1


    return a