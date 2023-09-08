# https://leetcode.com/problems/3sum/description/
# Solved: 2023-09-08

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            l_ptr = i+1
            r_ptr = len(nums)-1
            while l_ptr != r_ptr:
                if nums[i] + nums[l_ptr] + nums[r_ptr] == 0:
                    triplet = [nums[i], nums[l_ptr], nums[r_ptr]]
                    if triplet not in ans:
                        ans.append(triplet)
                    r_ptr -= 1
                elif nums[i] + nums[l_ptr] + nums[r_ptr] > 0:
                    r_ptr -= 1
                else:
                    l_ptr += 1
        return ans