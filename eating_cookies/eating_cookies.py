'''
Input: an integer
Returns: an integer


'''
# O(n) time, O(n) space
def eating_cookies(n, cache =None):

    if n < 0:
        return 0
    elif n == 0:
        return 1

    # check to si if answer is already stored in cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache= {i: 0 for i in range(n+1)}
        #store answers in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n-3, cache)

    return  cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50   

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")




# # O(3^n) time, O(3^n) space
# def eating_cookies(n):

#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:

#         return  eating_cookies(n-1) + eating_cookies(n - 2) + eating_cookies(n-3)