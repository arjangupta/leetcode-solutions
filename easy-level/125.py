# https://leetcode.com/problems/valid-palindrome/
# Solved: 2023-09-02

class Solution:
    def isPalindrome(self, s: str) -> bool:
        fwd_str = ""
        bkwd_str = ""
        s = s.lower()
        i_bkwd = len(s) - 1
        for i_fwd in range(len(s)):
            if s[i_fwd].isalpha() or s[i_fwd].isnumeric():
                fwd_str += s[i_fwd]
            if s[i_bkwd].isalpha() or s[i_bkwd].isnumeric():
                bkwd_str += s[i_bkwd] 
            i_bkwd -= 1
        return fwd_str == bkwd_str