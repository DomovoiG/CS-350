#Austin Gallup
#HW 6 
#11/12/21
#Rod-cutting problem

# step 1) Naive recursion

import sys
import time
import random

def random_array(size):
    array = [1]
    
    for i in range(1, size):

        array.append(random.randrange(array[i-1], array[i-1]*2))
    
    return array


def max(x, y):
    return x if (x > y) else y

def cutRod(price, n):
    if( n <= 0):
        return 0
    max_val = -sys.maxsize-1

    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i -1))

    return max_val



#step 2) memoize

INT_MIN = -32767

def cutRodMemoized(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val 
    
    return val[n]


for i in range(10, 26):
    arr = random_array(i)
    size = len(arr)
    start_time = time.time()
    print(cutRod(arr, size))
    print("recursion time: ", time.time()-start_time)

    start_time = time.time()
    print("memoized time: ", time.time()-start_time)