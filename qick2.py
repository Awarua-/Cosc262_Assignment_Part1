__author__ = 'Dion'
import random
from time import time, clock

c = 0
### a : array list containing data values
### n : integer value
### the function 'out' prints values in the array 'a'
### from a[1] ... a[n]
def out(a, n):
    for i in range(1, n+1):
        print (a[i], end=" ")
    print ('\n')


### a     : array list containing data values
### left  : integer value
### right : integer value
### the function 'sort' sorts values in array 'a'
### by recursively partitioning left and right side by pivot
def sort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        sort(a, left, pivot - 1)        #call sort on left  side of pivot
        sort(a, pivot + 1, right)       #call sort on right side of pivot


### a     : array list containing data values
### left  : integer value
### right : integer value
### the function 'partition' filters data values in the array 'a' from
### a[left] ... a[right], such that left side is smaller than pivot
### and right side is larger than pivot.
def partition(a, left, right):
    pivot      = a[left]         #stores the pivot value
    leftIndex  = left            #pointer starting from the left, going right
    rightIndex = right + 1       #pointer starting from the right, going left
    global c
    #if two pointers meet, then finish
    while leftIndex < rightIndex:
        rightIndex = rightIndex - 1

        #while a value from right is bigger than the pivot, decrement the rightIndex
        while a[rightIndex] >= pivot and leftIndex is not rightIndex:
            rightIndex = rightIndex - 1

        #if the pointers do not meet, move smaller value from right to the left
        if leftIndex is not rightIndex:
            a[leftIndex] = a[rightIndex]
            leftIndex += 1

        #while a value from left is smaller than the pivot, increment the leftIndex
        while a[leftIndex] <= pivot and leftIndex is not rightIndex:
            leftIndex = leftIndex + 1

        #if the pointers do not meet, move the larger value from left to the right
        if leftIndex is not rightIndex:
            a[rightIndex] = a[leftIndex]

    #put pack the pivot in the middle
    a[leftIndex] = pivot
    return leftIndex

### main function that calls quick sort
def main(n):

    a=[]                       #this is the array list to store values
    #populate the array 'a' with random numbers in range [0, 99]
    for i in range(0, n + 1):
        a=a+[int(100*random.random())]

    out(a, n)       #print current list of values in the array before sort
    t=clock()
    sort(a, 1, n)      #call quick sort
    out(a, n)       #print current list of values in the array after sort
    print ('time ',clock()-t)

n = int(input('input n '))
while n != 0:
    main(n)
    n = int(input('input n '))