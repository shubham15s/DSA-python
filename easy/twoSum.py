from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output.append(i)
        #             output.append(j)
        #             return output
        # optimised approach using hash map
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


nums = [2, 7, 11, 15]
target = 9
output = Solution().twoSum(nums, target)
print(output)
