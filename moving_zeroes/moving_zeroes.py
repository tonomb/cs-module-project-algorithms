'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # check if number is not 0, if true append it to new array
    # if they are zero add it to zeros array
    # count length of non zero array
    # append both arrays 
    non_zero = []
    zero =[]

    for i in arr:
        if i == 0:
            zero.append(i)
        else:
            non_zero.append(i)
        
    return non_zero + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")