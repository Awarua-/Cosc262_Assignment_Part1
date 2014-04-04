# This is a template for running experiments.
# Each program is run once. You should run each program five times or
# more and take the average time.

import random

import heapsort
import quicksort
import mergesort
import change_base
import radixsort
import radixquicksort


def run_quicksort(n, a):
    print("quicksort start")
    quicksort.main(n, a)
    print('quicksort done' + "\n")


def run_mergesort(n, a):
    print("mergesort start")
    mergesort.main(n, a)
    print('mergesort done' + "\n")


def run_heapsort(n, a):
    print("heapsort start")
    heapsort.main(n, a)
    print('heapsort done' + "\n")


def run_radixsort(a, base, max_num_len):
    print("radix-" + str(base) + "-sort start")
    radixsort.main(a, base, max_num_len)
    print("radix-" + str(base) + "-sort done" + "\n")


def run_radixquicksort(n, a, max_len):
    print("radix-quicksort start")
    radixquicksort.main(n, a, max_len)
    print('radix-quicksort done' + "\n")


def main(n):
    # main program

    data = []
    for i in range(0, n + 1):
        data += [int(100 * random.random())]
    print()

    # ## Experiment on heapsort ##
    # a = []
    # for i in range(0, n + 1):
    #     a += [data[i]]
    # run_heapsort(n, a)

    ## Experiment on quicksort ##
    a = []
    for i in range(0, n + 1):
        a += [data[i]]
    run_quicksort(n, a)

    # ## Experiment on mergesort ##
    # a = []
    # for i in range(0, n + 1):
    #     a += [data[i]]
    # run_mergesort(n, a)

    ##Experiment on Radix-10 sort##
    base = 10
    a = change_base.main(data, base, 99)
    run_radixsort(a, base, len(change_base.change_base(99, base)))

    ##Experiment on Radix-2 sort##
    base = 2
    a = change_base.main(data, base, 99)
    run_radixsort(a, base, len(change_base.change_base(99, base)))

    ##Experiment on Radix-quick sort##
    base = 2
    a = change_base.main(data, base, 99)
    run_radixquicksort(n, a, len(change_base.change_base(99, base)))

    # ##Experiment on Radix-1 sort##
    # base = 1
    # a = change_base.main(data, base, 99)
    # run_radixsort(a, base, len(change_base.change_base(99, base)))

n = int(input('input n '))
while n != 0:
    main(n)
    n = int(input('input n '))