# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l_ptr = 0
        r_ptr = l_ptr + 2
        total_water = 0
        while r_ptr < len(height):
            if height[l_ptr + 1] > height[l_ptr]:
                l_ptr += 1
                r_ptr += 1
            elif r_ptr + 1 >= len(height) or height[r_ptr + 1] < height[r_ptr] or height[r_ptr] > height[l_ptr]:
                temp_r_ptr = r_ptr
                if r_ptr + 1 < len(height) and height[r_ptr + 1] < height[r_ptr] and height[l_ptr] > height[r_ptr]:
                    while temp_r_ptr < len(height):
                        if height[temp_r_ptr] >= height[l_ptr]:
                            r_ptr = temp_r_ptr
                            break
                        temp_r_ptr += 1
                shorter_end = min(height[l_ptr], height[r_ptr])
                l_ptr += 1
                while l_ptr != r_ptr:
                    height_diff = shorter_end - height[l_ptr]
                    if height_diff > 0:
                        total_water += height_diff
                    l_ptr +=1
                if temp_r_ptr == len(height):
                    break
                l_ptr = r_ptr
                r_ptr = l_ptr + 2
            else:
                r_ptr += 1
        return total_water
            