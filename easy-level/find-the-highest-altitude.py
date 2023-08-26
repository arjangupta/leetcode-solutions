# https://leetcode.com/problems/find-the-highest-altitude/
# Solved: 2023-08-26

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = 0
        for height_change in gain:
            current_altitude += height_change
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude
        return highest_altitude