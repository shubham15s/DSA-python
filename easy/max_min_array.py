def get_max_min_arr(arr):

    #approach 1: comparing with min and max
    min = float("inf")
    max = float("-inf")
    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max
    
    #approach 2: sorting the element first and then take min and max from index
    # arr.sort()
    # min = arr[0]
    # max = arr[-1]
    # return min, max

A = [4, 9, 6, 5, 2, 3]
min, max = get_max_min_arr(A)
print(min, "  ", max)