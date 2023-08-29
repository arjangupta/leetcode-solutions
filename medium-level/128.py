# https://leetcode.com/problems/longest-consecutive-sequence/
# Solved: 2023-08-28

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set()
        for num in nums:
            num_set.add(num)
        longest = 1
        # Need to keep track of longest seq because
        # otherwise we will go over portions that
        # we have already checked
        longest_seq = set()
        for num in nums:
            if num in longest_seq:
                continue
            curr_longest = 1
            start_point = num
            # Counting down is important, by counting up you
            # don't catch truly longest subseq
            while (start_point - 1) in num_set:
                longest_seq.add(start_point - 1)
                curr_longest += 1
                start_point -= 1
            if curr_longest > longest:
                longest = curr_longest
        return longest