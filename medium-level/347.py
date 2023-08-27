# https://leetcode.com/problems/top-k-frequent-elements/
# Solved: 2023-08-26

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_hm = sorted(hashmap, key=hashmap.get, reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_hm[i])
        return ans