## Binary search: this algortihm allows to find a number in a set of ordered numbers. 
## It works by giving to the computer a number to find. If the mid number is higher or lower tan the target,
## the computer will find another mid number to compare discarding the rest of the numbers that doesn't enter in the range of,
## the low and high numbers. This algorithm uses recursion which means that the program will autoreferenciate itself with new parameters

def binary_search(list_of_numbers, low_number, high_number, target_number):
    ## If the low_number is higher than high_number then return false
    if low_number > high_number:  
        return False
    
    ## We have daclared a high number and a lower, but we need a number between them which is this
    mid_number = (low_number + high_number) // 2 

    ## If the index of mid number in the list of numbers is equal to the target number return True, which means that the computer found the number
    if list_of_numbers[mid_number] == target_number:
        return mid_number
    
    ## If the mid number is lower than the target, then call a recursive function wich means that,
    ## the program will start over but with different conditions, because now low_number is added 1
    elif list_of_numbers[mid_number] < target_number:
        return binary_search(list_of_numbers, low_number + 1, high_number, target_number)
    
    ## The same case than before but now we rest 1 to the high_number
    elif list_of_numbers[mid_number] > target_number:
        return binary_search(list_of_numbers, low_number, high_number - 1, target_number)

    



if __name__ == "__main__":
    ## This is the input of the user, the machine will find this number
    target_number = int(input("Choose a number between 0 and 1000: ")) 
    
    ## This statement returns a list in the range of 0 and 1000
    list_of_numbers = [*range(0, 1000 + 1)] 

    ## the result of the function is stored in a variable, this function has to work with the index of the list
    ## because its easy to the computer working with indexes than with the list 
    ## for instance: if you have repeated numbers, the computer won't be able to give precise results
    ## because when you give the instruction of a mathematical operation the computer may be "confused"
    found = binary_search(list_of_numbers, 0, len(list_of_numbers), target_number)
    print(f"The computer found your number and it is {found}")
