'''
Question: A peak element is an element that is greater than its neighbors. Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index. The array may contain multiple peaks, in that case, return the index to any one of the peaks.
Example Input: [1, 2, 3, 1]
Example Output: 2 (3 is a peak element)
'''


def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1 
        else:
            right = mid 

    return left


print(find_peak_element([1, 2, 3, 1])) # 2