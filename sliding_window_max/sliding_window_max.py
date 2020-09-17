'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# O(n^2)
def sliding_window_max(nums, k):
    # get the max out of k
    # how many times does the window have to iterate, how does it stop?

    passes = len(nums) - k + 1
    max_nums = [ ]

    for i in range(passes): # O(n)
        copy = nums[:]
        max_num = max(copy[i : i + k]) # O(n)   
        max_nums.append(max_num)
    
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
