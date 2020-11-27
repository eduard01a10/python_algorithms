import random

# This function will perform the partition of the array
def partition(arr, left, right):
    
    # This variable will start to count before the array stars
    # because we want it to start from the first element
    i = left - 1

    # The pivot represent a choosen number to make the partitions
    pivot = arr[right]

    # This for loop will go to through all the array from 0 to n - 1
    for j in range(left, right):
        
        # if the number is less or equal to the pivot then move one space the variable i
        # after that, make a swap between the number in the position of j and the position of i
        # this means that all the numbers that are lower than the pivot will be in the left and all the
        # numbers grater than the pivot will be at the right
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # this swaping means that the pivot that is: n - 1 will be changed by i + 1
    # making the pivot at the center of the array, this pivot will not be moved because it is now ordered
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

def quicksort(arr, left, right):
    
    # if the lenght of the array is equal to 1 it means that the array contains only 1 argument
    # therefore it is ordered
    if len(arr) == 1:
        return arr

    # If the left part of the array is lower than the right part then:
    if left < right:
        
        # save the partition function in a variable
        p = partition(arr, left, right)

        # This is where the recursive functions are called it means that 
        # the partition function will be executed again and again but with one difference
        # when a pivot is defined the recursive function will star one space at the right
        # or one space at the left 
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)

    return arr

if __name__ == "__main__":
    arr = [*range(0, 1000+1)]
    random.shuffle(arr)

    n = len(arr)

    # We pass it three arguments, the array, the first index where the algorithm will start
    # and the last index of the array
    result = quicksort(arr, 0, n-1)
    print(result)
