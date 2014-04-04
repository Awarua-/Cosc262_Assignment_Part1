__author__ = 'Dion'

from time import clock


def sort(a, max_len, current_len, result):
    if current_len == max_len:
        return result.extend(a)
    else:
        left = []
        right = []
        for i in a:
            if list(i)[current_len] == '0':
                left.append(i)
            else:
                right.append(i)
        sort(left, max_len, current_len + 1, result)
        sort(right, max_len, current_len + 1, result)



def main(n, a, max_len):

    # {main program}
    t = clock()
    result = sort(a[1:], max_len, current_len=0, result=[])
    print(result)
    print('time ', clock()-t)
