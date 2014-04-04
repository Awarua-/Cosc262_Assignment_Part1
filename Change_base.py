__author__ = 'Dion'


def change_base(num, base):
    num_rep = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k',
               21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v',
               32: 'w', 33: 'x', 34: 'y', 35: 'z'}
    new_num = ''
    current = num
    if base == 1:
        new_num = '1' * num
    else:
        while current != 0:
            remainder = current % base
            if 36 > remainder > 9:
                remainder_ = num_rep[remainder]
            else:
                remainder_ = str(remainder)
            new_num = remainder_ + new_num
            current = int(current / base)

    return new_num


def check_length(num, base, max_length):
    new_num = change_base(num, base)
    if len(new_num) < max_length:
        n = max_length - len(new_num)
        new_num = (n * '0') + new_num

    return new_num


def main(list_of_nums, base, max_num):
    new_num_list = []
    len_max_num = len(change_base(max_num, base))
    for i in list_of_nums:
        new_num_list.append(check_length(i, base, len_max_num))

    return new_num_list
