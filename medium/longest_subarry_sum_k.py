def lenOfLongSubarr ( arr, n, k) : 
    sum_map = {}
    sum = 0
    max_len = 0
    
    for i in range(n):
        sum += arr[i]
        if sum == k:
            max_len = max(max_len,i+1)
        rem = sum - k
        if rem in sum_map:
            length  = i - sum_map[rem]
            max_len = max(max_len,length)
        if sum not in sum_map:
            sum_map[sum] = i
    return max_len

arr = [10, 5, 2, 7, 1, 9]
n= 6
k = 15

print("longest sub array sum :",lenOfLongSubarr(arr, n, k))