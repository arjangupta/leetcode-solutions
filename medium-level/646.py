# https://leetcode.com/problems/maximum-length-of-pair-chain/
# Solved: 2023-08-26

from typing import List

class Solution:
    def by_first_elem(self, arr: List[int]) -> int:
        return arr[0]

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_pairs = sorted(pairs, key=self.by_first_elem)
        chains = [1] * len(pairs)
        for i in range(len(pairs)-1,-1,-1):
            for j in range(i+1, len(pairs)):
                if sorted_pairs[i][1] < sorted_pairs[j][0]:
                    chains[i] = max(chains[i],1+chains[j])
        return max(chains)