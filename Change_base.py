__author__ = 'Dion'

import _collections


def change_base(num, base):
    new_num = _collections.deque([])
    current = num

    while current != 0:
        remainder = current % base
        new_num.appendleft(remainder)
        current = current // base

    return new_num


def check_length(num, base, max_length):
    new_num = change_base(num, base)
    if len(new_num) < max_length:
        n = max_length - len(new_num)
        for _ in range(0, n):
            new_num.appendleft(0)

    return list(new_num)


def main(list_of_nums, base, max_num, quickradix):
    new_num_list = []
    if quickradix is True:
        max_length = len(change_base(max_num, base))
        for i in list_of_nums:
            new_num_list.append(check_length(i, base, max_length))

        return new_num_list, max_length
    else:
        max_length = len(change_base(max_num, base))
        for i in list_of_nums:
            new_num_list.append(list(change_base(i, base)))

        return new_num_list, max_length


def revert_base(list_of_nums, base):
    org_nums = []
    for i in list_of_nums:
        org_num = 0
        power = 0
        for j in i:
            if j != 0:
                org_num += j * (base ** power)
                power += 1
            else:
                power += 1
        org_nums.append(org_num)
    return org_nums


