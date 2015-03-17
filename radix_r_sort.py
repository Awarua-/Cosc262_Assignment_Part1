__author__ = 'Dion'


def main(a, base, max_len):
    """
    Runs the algorithm
    :param a: the data array
    :param base: the base of the data in a
    :param max_len: the maximum number of places in the largest data entry in a
    :return:
    """

    # Create an array of buckets according to the base
    buckets = []
    for _ in range(0, base):
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