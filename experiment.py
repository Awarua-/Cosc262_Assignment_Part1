# This is a template for running experiments.
# Each program is run once. You should run each program five times or
# more and take the average time.

import random
from time import clock
import heapsort
import quicksort
import mergesort
import quickradixsort
import radix_r_sort
import change_base


def main(n):
    # main program

    min = 1
    max = n // 5
    radix_max_base = 100

    heapsort_results = [[], []]
    quicksort_results = [[], []]
    doublequicksort_results = [[], []]
    mergesort_results = [[], []]
    radix2sort_results = []
    radix3sort_results = []
    radix4sort_results = []
    quickradixsort_results = []
    radixsort_results = [[] for _ in range(radix_max_base // 5)]

    for i in range(10):

        data = []
        for i in range(0, n + 1):
            data += [random.randint(min, max)]

        ## Experiment on heapsort ##
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        heapt, heapc = heapsort.main(n, a)
        heapsort_results[0].append(heapt)
        heapsort_results[1].append(heapc)


        ## Experiment on quicksort ##
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        quickt, quickc, dquickt, dquickc = quicksort.main(n, a)
        quicksort_results[0].append(quickt)
        quicksort_results[1].append(quickc)
        doublequicksort_results[0].append(dquickt)
        doublequicksort_results[1].append(dquickc)

        ## Experiment on mergesort ##
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        merget, mergec = mergesort.main(n, a)
        mergesort_results[0].append(merget)
        mergesort_results[1].append(mergec)


        ##Experiment on Radix-2 sort##
        base = 2
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        radix2t = clock()
        x = bin(max)[2:]
        sorted_a = radix_r_sort.main(a, base, len(x))
        radix2sort_results.append(clock() - radix2t)

        ##Experiment on Radix-3 sort##
        base = 3
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        radix3t = clock()
        num_max_len = len(list(change_base.change_base(max, base)))
        sorted_a = radix_r_sort.main(a, base, num_max_len)
        radix3sort_results.append(clock() - radix3t)

        ##Experiment on Radix-4 sort##
        base = 4
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        radix4t = clock()
        num_max_len = len(list(change_base.change_base(max, base)))
        sorted_a = radix_r_sort.main(a, base, num_max_len)
        radix4sort_results.append(clock() - radix4t)

        ##Experiment on Radix-r sort##
        counter = 0
        for i in range(5, radix_max_base + 1, 5):

            base = i
            a = []
            for i in range(0, n + 1):
                a += [data[i]]
            radixt = clock()
            num_max_len = len(list(change_base.change_base(max, base)))
            sorted_a = radix_r_sort.main(a, base, num_max_len)
            radixsort_results[counter].append(clock() - radixt)
            counter += 1

        ##Experiment on Quick-Radix sort##
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        quickradixt = clock()
        x = bin(max)[2:]
        length = len(x)
        sorted_a = quickradixsort.main(a, length)
        quickradixsort_results.append(clock() - quickradixt)

    return heapsort_results, quicksort_results, doublequicksort_results, mergesort_results, radix2sort_results,\
           radix3sort_results, radix4sort_results, quickradixsort_results, radixsort_results, radix_max_base
