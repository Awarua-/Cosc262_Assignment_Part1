__author__ = 'Dion'


def sort(a, max_len, current_len, result):
    if current_len < 0:
        return result.extend(a)
    else:
        left = []
        right = []
        for i in a:
            if (i >> current_len) % 2 == 0:
                left.append(i)
            else:
                right.append(i)
        sort(left, max_len, current_len - 1, result)
        sort(right, max_len, current_len - 1, result)
    return result


def main(a, max_len):

    # {main program}
    result = sort(a[1:], max_len, current_len=max_len, result=[])
    assert result[1:] == sorted(result[1:]), "List not sorted, error!!!!!!!!!!"
    return result