__author__ = 'Dion'


def main(data, base, max_len):
    """
    Runs the algorithm
    :param data: the data array
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
        # sort current place into buckets
        for k in data[1:]:
            x = (k // base ** i) % base
            buckets[x].append(k)

        # reset the data array
        # copy the results out of the buckets back into the data array
        # and empty the bucket array
        data = data[:1]
        for j in buckets:
            r, j[:] = j[:], []
            data.extend(r)

        i += 1

    return data