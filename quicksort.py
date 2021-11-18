#5.2 problem 10 solution
# implementation of quicksort using python
#unsorted list of integers to be sorted.

def partition(array,start, end):

    pivotIndex = (start-1)
    pivotValue = array[end]    
    for i in range(start, end):
        if array[i] <= pivotValue:
            pivotIndex = pivotIndex + 1
            array[pivotIndex], array[i] = array[i], array[pivotIndex]
        
    array[pivotIndex+1], array[end] = array[end], array[pivotIndex+1]
    return pivotIndex


def quickSort(array, start, end):

    if len(array) == 1:
        return array
    if start < end:
    
        index = partition(array, start, end)
    
        quickSort(array, start, index-1)
        quickSort(array, index+1, end)
    
    return
import time
import random

for k in range(0, 10):
    array = []
    for x in range(0, random.randint(1000, 100000)):
        array.append(random.randint(0, 1000))
    start_time = time.time()
    quickSort(array, 0, len(array)-1)
    print("size of array: %s" % len(array))
    print("---%s seconds---" % (time.time() - start_time))
