#Brute force string matching algorithm implementation.
#Austin Gallup, 10/28/21


stringToMatch = "With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea." 

print(stringToMatch)

def matchString(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        index = i
        for k in range(index-1):
            print(end = "-")
        for j in range(len(pattern)):
            if text[index] == pattern[j]:
                print(end = pattern[j])
                index += 1
            else:
                break
            if index-1 == len(pattern):
                return i
        
        print()
    return -1   

import time

start_time = time.time()

print("----%s seconds---"%(time.time() - start_time))