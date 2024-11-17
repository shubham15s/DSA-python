'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

def longestConsecutive(nums):
    n = len(nums)
    if n == 0:
        return 0
    longest = 1
    num_set = set()
    for i in range(n):
        num_set.add(nums[i])  
    for num in num_set:
        if num - 1 not in num_set:
            count = 1
            x = num
            while x + 1 in num_set:
                x += 1
                count += 1
            longest = max(longest,count)
    return longest
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))