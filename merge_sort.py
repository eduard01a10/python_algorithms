## Merge sort: this is one of the most eficient algorithms of sorting because it has a O(nlogn) it works by divide and conquer.
## The principle is to divide a list until we have a single argument in the list, then compare it with the other single list
## and sort it. 

import random

def merge_sort(list_numbers):
    
    ## the index of the list must be grater than 1 
    if len(list_numbers) > 1:

        ## Mid is where the list is divided in two lists
        mid = len(list_numbers) // 2
        
        ## The result will give two lists, one at the left and one at the right with list slice we can "cut" the slice we dont need
        left = list_numbers[:mid]
        right = list_numbers[mid:]

        ## Recursive functions are called so we can repeat the lines of code, it will give more divided lists until we reach a single list,
        ## with one element
        merge_sort(left)
        merge_sort(right)

        #We declare 2 initial conditions for the sublists
        i = 0
        j = 0

        #We declare 1 initial condition for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_numbers[k] = left[i]
                i += 1
            else:
                list_numbers[k] = right[j]
                j += 1
            
            k += 1

        # This block of code will compare the left part of the sublist, it will check if the
        while i < len(left):
            list_numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_numbers[k] = right[j]
            j += 1
            k += 1

    return list_numbers

if __name__ == "__main__":
    list_numbers = [*range(0, 1000 + 1)]
    random.shuffle(list_numbers)
    
    
    list_ordered = merge_sort(list_numbers)
    print(list_ordered)