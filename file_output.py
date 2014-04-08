__author__ = 'Dion'


import experiment


def avg(list_of_elements):
    return sum(list_of_elements) / len(list_of_elements)

def main():

    file = open("results.txt", "w")


    for n in range(1000, 20001, 1000):
        heapsort_results,  quicksort_results, doublequicksort_results, mergesort_results, radix10sort_results, \
        quickradixsort_results, radixsort_results, radix_max_base = experiment.main(n)

        file.write("\n Results for " + str(n) + " list size \n CPU time \n")
        file.write(str(avg(heapsort_results[0])) + '\n')
        file.write(str(avg(quicksort_results[0])) + '\n')
        file.write(str(avg(doublequicksort_results[0])) + '\n')
        file.write(str(avg(mergesort_results[0])) + '\n')
        file.write(str(avg(radix10sort_results)) + '\n')
        file.write(str(avg(quickradixsort_results)) + '\n')

        for i in range(2, radix_max_base + 1):
            file.write(str(avg(radixsort_results[i - 2])) + '\n')

        file.write("\n Comparisons \n")
        file.write(str(int(avg(heapsort_results[1]))) + '\n')
        file.write(str(int(avg(quicksort_results[1]))) + '\n')
        file.write(str(int(avg(doublequicksort_results[1]))) + '\n')
        file.write(str(int(avg(mergesort_results[1]))) + '\n')

        print("finished " + str(n))

    file.close()

main()