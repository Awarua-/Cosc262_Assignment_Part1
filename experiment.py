# This is a template for running experiments.
# Each program is run once. You should run each program five times or
# more and take the average time.

import random
from time import clock
import heapsort
import quicksort
import mergesort
import radix_r_sort
import change_base
import quickradixsort
import radix_10_sort





def main(n):
    # main program

    min = 1
    max = 1000
    radix_max_base = 30

    heapsort_results = [[], []]
    quicksort_results = [[], []]
    doublequicksort_results = [[], []]
    mergesort_results = [[], []]
    radix10sort_results = []
    quickradixsort_results = []
    radixsort_results = [[] for _ in range(radix_max_base - 1)]

    for i in range(5):

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

        ##Experiment on Radix-10 sort##
        base = 10
        a = []
        for i in range(0, n + 1):
            a += [data[i]]
        radix10t = clock()
        sorted_a = radix_10_sort.main(a, base, len(str(max)))
        radix10sort_results.append(clock() - radix10t)

        ##Experiment on Radix-r sort##
        for i in range(2, radix_max_base + 1):
            base = i
            a = []
            for i in range(0, n + 1):
                a += [data[i]]
            radixt = clock()
            base_a, len_max_num = change_base.main(a, base, max, quickradix=False)
            sorted_a = radix_r_sort.main(base_a, base, len_max_num)
            revert_a = change_base.revert_base(sorted_a, base, len_max_num)
            radixsort_results[base - 2].append(clock() - radixt)

        ##Experiment on Quick-Radix sort##
        quickradixt = clock()
        base = 2
        a, len_max_num = change_base.main(data, base, max, quickradix=True)
        sorted_a = quickradixsort.main(a, len_max_num)
        revert_a = change_base.revert_base(sorted_a, base, len_max_num)
        quickradixsort_results.append(clock() - quickradixt)

    return heapsort_results, quicksort_results, doublequicksort_results, mergesort_results,radix10sort_results, \
           quickradixsort_results, radixsort_results, radix_max_base
