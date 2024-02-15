# https://leetcode.com/problems/binary-search/description/
# Solved: 2024-02-14

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        half_index = int(len(nums)/2)
        if nums[half_index] == target:
            return half_index
        if half_index == 0:
            return -1
        l_result = self.search(nums[0:half_index], target)
        r_result = self.search(nums[half_index:], target)
        if l_result > -1:
            return l_result
        elif r_result > -1:
            return half_index + r_result
        else:
            return -1