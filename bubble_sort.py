## Bubble sort: as far as I know this sorting method is the first one when a human wants to sort something, in the real world this looks like
## easy but in CS this algorithm is the worst due to the worst case which is O(n^2) in a large set of numbers this algorithm will take 
## a long time to complete 

import random

def bubble_sort(list_numbers):
    n = len(list_numbers)
    
    ## First for loop which takes the index of the set of numbers
    for i in range(n):

        ## Second for loop which it wil reduce the last number of the set of numbers and start again
        for j in range(0, n - i - 1):

            ## This is the swaping, it wil replace the higher number to the left
            if list_numbers[j] > list_numbers[j + 1]:

                ## This line of code represents the number j equals to j + 1 and j + 1 equal to j
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    
    return list_numbers 

if __name__ == "__main__":
    list_numbers = [*range(1, 100 + 1)]
    random.shuffle(list_numbers)
    
    list_ordered = bubble_sort(list_numbers)
    print(list_ordered)
    