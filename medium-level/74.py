# https://leetcode.com/problems/search-a-2d-matrix/
# Solved: 2024-02-15

from typing import List

class Solution:
    def searchRow(self, row:List[int], target:int) -> bool:
        mid_idx = int(len(row)/2)
        if row[mid_idx] == target:
            return True
        if mid_idx == 0:
            return False
        left_arr = row[0:mid_idx]
        if self.searchRow(left_arr, target):
            return True
        right_arr = row[mid_idx:]
        if self.searchRow(right_arr, target):
            return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mid_row = int(len(matrix)/2)
        if self.searchRow(matrix[mid_row], target):
            return True
        if mid_row == 0:
            return False
        left_rows = matrix[:mid_row]
        if self.searchMatrix(left_rows, target):
            return True
        right_rows = matrix[mid_row:]
        if self.searchMatrix(right_rows, target):
            return True
        return False