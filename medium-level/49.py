# https://leetcode.com/problems/group-anagrams/
# Solved: 2023-08-31

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            word_arr = [c for c in word]
            word_arr = sorted(word_arr)
            sorted_word = ''.join(word_arr)
            if sorted_word in table:
                table[sorted_word].append(word)
            else:
                table[sorted_word] = [word]
        ans = []
        for key in table:
            arr = table[key]
            ans.append(arr)
        return ans