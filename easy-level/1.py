# https://leetcode.com/problems/two-sum/
# Solved: 2023-08-29

# O(n) solution

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {}
        for i in range(len(nums)):
            if nums[i] not in num_table:
                num_table[nums[i]] = [i]
            else:
                num_table[nums[i]].append(i)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_table:
                if diff == nums[i]:
                    if len(num_table[diff]) > 1:
                        duplicate_idx_list = num_table[diff]
                        for j in duplicate_idx_list:
                            if j != i:
                                return [i,j]
                else:
                    return [i,num_table[diff][0]]
        return []