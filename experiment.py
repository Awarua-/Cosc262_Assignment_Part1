# This is a template for running experiments.
# EAch program is run once. You should run each program five times or
# more and take the average time.

import random
import heapsort
import quicksort
import mergesort

from time import time, clock



def out(n, a):
    for i in range(1, n + 1):
        print(a[i])
    print('\n')


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


def main(n):
    # main program

    data = []
    for i in range(0, n + 1):
        data += [int(100 * random.random())]
    print()


    ## Experiment on heapsort ##
    a = []
    for i in range(0, n + 1):
        a += [data[i]]
    run_heapsort(n, a)



    ## Experiment on quicksort ##
    a = []
    for i in range(0, n + 1):
        a += [data[i]]
    run_quicksort(n, a)



    ## Experiment on mergesort ##
    a = []
    for i in range(0, n + 1):
        a += [data[i]]
    run_mergesort(n, a)


n = int(input('input n '))
while n != 0:
    main(n)
    n = int(input('input n '))