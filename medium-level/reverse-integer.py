# https://leetcode.com/problems/reverse-integer/
# Solved date: 2023-08-25

class Solution:
    def reverse(self, x: int) -> int:
        x_arr = [c for c in str(x)]
        x_arr.reverse()
        if x_arr[-1] == '-':
            x_arr = x_arr[0:-1]
            x_arr.insert(0, '-')
        ans = int(''.join(x_arr))
        if (ans > 2147483647) or (ans < -2147483648):
            return 0
        return ans