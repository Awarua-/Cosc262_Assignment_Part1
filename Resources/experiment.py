# This is a template for running experiments.
# EAch program is run once. You should run each program five times or
# more and take the average time.

import random
from time import time, clock


c = 0


def out(a):
    for i in range(1, n+1):
        print(a[i])
    print('\n')


def run_quicksort():
    print('\n')
    print('quicksort done')


def run_mergesort():
    print('\n')
    print('mergesort done')


def run_heapsort():
    print('\n')
    print('heapsort done')

 
# main program 
n = int(input('input n '))
data = []
for i in range(0, n + 1):
    data += [int(100 * random.random())]

out(data)

## Experiment on heapsort ##
a = []
for i in range(0,n+1):
    a += [data[i]]
c = 0
t = clock()
run_heapsort()
#out(a)
print('time ', clock()-t, 'c=', c)

## Experiment on quicksort
a = []
for i in range(0, n + 1):
    a += [data[i]]
c = 0
t = clock()
run_quicksort()
#out(n)
print('time ', clock() - t, 'c=', c)

## Experiment on mergesort ##
a = []
for i in range(0, n + 1):
    a += [data[i]]
c = 0
t = clock()
run_mergesort()
#out(n)
print('time ', clock() - t, 'c=', c)
n = input('finished ')