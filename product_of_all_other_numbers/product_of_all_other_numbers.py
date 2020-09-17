'''
Input: a List of integers
Returns: a List of integers
'''

# O(n^2)
def product_of_all_other_numbers(arr):
    # not multiplying by the index at value is equal to multiplying by 1 
    # how do you change the value at a index without changing the original array
    # once the value is changed multiply all numbers 

    multiplied = [0 for _ in arr]  # O(n)

    for i in range(len(arr)): # O(n)
        copy = arr[:]
        # copy has a value of 1 at the index, original array not changed
        copy[i] = 1
        # multiply all numbers in the copy array
        result = 1
        for x in copy: # O(n)
            result *= x
       
        multiplied[i] = result
        
    return multiplied


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
