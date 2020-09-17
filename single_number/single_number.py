'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# O(n^2)
# def single_number(arr):
#     # loop over array
#     # add number to new array
#     # if new number is already there pop existing number
#     # otherwise add number 
#     # the resulting array should only have one number

#     not_seen = []

#     for i in arr:
#         if i in not_seen:  # O(n)
#             not_seen.remove(i)  
#         else:
#             not_seen.append(i)

#     return not_seen[0]

#O(n)
def single_number(arr):
    s = set()
    for num in arr:
        if num in s: # O(1)
            s.remove(num)
        else:
            s.add(num)

    return list(s)[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# 