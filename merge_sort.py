## Merge sort: this is one of the most eficient algorithms of sorting because it has a O(nlogn) it works by divide and conquer.
## The principle is to divide a list until we have a single argument in the list, then compare it with the other single list
## and sort it. 

import random

def merge_sort(arr):
    
    # If the lenght of the array is greater than 1 it means that is an array with multiple arguments
    if len(arr) > 1:

        # The array is divided in two sub-arrays
        mid = len(arr) // 2
        
        # After dividing the array in two parts, we're going to store both parts in variables
        # one at the left and one at the right
        left = arr[:mid]
        right = arr[mid:]

        # Recursive functions are called so we can repeat the lines of code, it will give more divided lists until we reach a single list,
        # with one element
        merge_sort(left)
        merge_sort(right)

        # We declare 2 initial conditions for the sub-arrays
        i = 0
        j = 0

        # We declare 1 initial condition for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1

        # This block of code will compare the left part of the sublist, it will check if the
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    arr = [*range(0, 100 + 1)]
    random.shuffle(arr)
    print(arr)
    
    
    list_ordered = merge_sort(arr)
    print(list_ordered)