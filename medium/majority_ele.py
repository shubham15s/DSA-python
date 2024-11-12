'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
from typing import List
def majorityElement( nums: List[int]) -> int:
        n = len(nums)
        count = 0
        ele = None

        for i in range(n):
            if count == 0:
                count = 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -= 1
        count1 = 0
        for i in range(n):
            if nums[i] == ele:
                count1 += 1
        if count1 > n/2:
            return ele
        
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))