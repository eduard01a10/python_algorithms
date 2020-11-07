## Insertion sort: this algorithm allows to sort a disordered list by sorting the numbers like if it were a hand of poker cards
## the computer takes the first number and compares it whit the number at the right and if the number at the right is higher
## it goes to the left and so on.

## The radom method is invocated
import random

def insertion_sort(list_of_numbers):
    
    ## For every index in the list of numbers do something
    for index in range(1, len(list_of_numbers)):
        ## the current value is equal to the first number in the list
        current_value = list_of_numbers[index]
        ## the current position is equal to the first index in the list
        current_position = index

        ## while the current position (index) is grater than 0 and the number of the list minus 1 is grater than the current value then 
        while current_position > 0 and list_of_numbers[current_position - 1] > current_value:
            ## The number of the current position in list is equal to the same number - 1
            list_of_numbers[current_position] = list_of_numbers[current_position - 1]
            ## Rest the index - 1 a keep de loop going
            current_position -= 1

        list_of_numbers[current_position] = current_value
    
    return list_of_numbers

if __name__ == "__main__":
    list_of_numbers = [*range(0, 100 + 1)]
    random.shuffle(list_of_numbers)

    ordered_list = insertion_sort(list_of_numbers)
    print(ordered_list)