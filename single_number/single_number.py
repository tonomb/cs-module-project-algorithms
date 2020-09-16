'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # the array will always be an odd number 
    # how can I count if I already saw a number
    # I need someway to loop over each int

    # loop over array
    # add number to new array
    # if new number is already there pop existing number
    # otherwise add number 
    # the resulting array should only have one number

    not_seen = []

    for i in arr:
        if i in not_seen:
            not_seen.remove(i)
        else:
            not_seen.append(i)

    return not_seen[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")