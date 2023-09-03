# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solved: 2023-09-03

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_table = {}
        for i in range(len(numbers)):
            if numbers[i] not in num_table:
                num_table[numbers[i]] = [i]
            else:
                num_table[numbers[i]].append(i)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in num_table:
                if diff == numbers[i]:
                    if len(num_table[diff]) > 1:
                        duplicate_idx_list = num_table[diff]
                        for j in duplicate_idx_list:
                            if j != i:
                                return [i+1,j+1]
                else:
                    return [i+1,num_table[diff][0]+1]
        return []