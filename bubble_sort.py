## Bubble sort: as far as I know this sorting method is the first one when a human wants to sort something, in the real world this looks like
## easy but in CS this algorithm is the worst due to the worst case which is O(n^2) in a large set of numbers this algorithm will take 
## a long time to complete 

import random

def bubble_sort(list_numbers):
    # Define the lenght of the array it's necessary because the algorithms work with indexes
    n = len(list_numbers)
    
    ## First for loop which takes the index of the set of numbers this will go through all the index
    for i in range(n):

        ## Second for loop which it wil reduce the last number of the set of numbers and start again
        ## j is the second iterator this will go from 0 to n (the las index of the array) minus i minus 1 
        ## in order to acces to the last index of the array
        for j in range(0, n - i - 1):

            ## This if statement compares the number with the other at the right
            if list_numbers[j] > list_numbers[j + 1]:

                ## This line makes the swaping
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    
    return list_numbers 

if __name__ == "__main__":
    list_numbers = [*range(1, 100 + 1)]
    random.shuffle(list_numbers)
    
    list_ordered = bubble_sort(list_numbers)
    print(list_ordered)
    