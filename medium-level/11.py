# https://leetcode.com/problems/container-with-most-water/description/
# Solved: 2023-09-08

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max_area = 0
        l_ptr = 0
        r_ptr = len(height) - 1
        while l_ptr != r_ptr:
            width = r_ptr - l_ptr
            min_height = min([height[l_ptr], height[r_ptr]])
            current_area = width * min_height
            max_area = max(current_area, max_area)
            if min_height == height[l_ptr]:
                l_ptr += 1
            elif min_height == height[r_ptr]:
                r_ptr -= 1
            else: # same heights
                if height[l_ptr+1] > height[l_ptr]:
                    l_ptr += 1
                else:
                    r_ptr -= 1
        return max_area