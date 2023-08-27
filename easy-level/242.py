# https://leetcode.com/problems/valid-anagram/
# Solved: 2023-08-26

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        t_dict = {}
        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        return s_dict == t_dict