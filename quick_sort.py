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
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

def quicksort(arr, left, right):
    if len(arr) == 1:
        return arr

    if left < right:
        p = partition(arr, left, right)

        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)

    return arr

if __name__ == "__main__":
    arr = [*range(0, 1000+1)]
    random.shuffle(arr)
    #print(arr)

    n = len(arr)

    # We pass it three arguments, the array, the first index where the algorithm will start
    # and the last index of the array
    result = quicksort(arr, 0, n-1)
    print(result)
