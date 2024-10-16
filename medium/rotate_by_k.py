from typing import List


def rotate( nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    temp = [0]*n
    for i in range(n):
        temp[(i+k)%n] = nums[i]
    # Copy the temporary list back to the original list
    for i in range(n):
        nums[i] = temp[i]

nums = [1,2,3,4,5,6,7]
k = 3
sol = rotate(nums, k)

print(nums)