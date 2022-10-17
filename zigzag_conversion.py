# Exceeds the time limit
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result: str = ""
        for j in range(numRows):
            for i in range(len(s)):
                if 2*numRows - 2 == 0 or ((i) % (2*numRows - 2)) == j or (i % (2*numRows - 2) == (2*numRows - 2 - j)):
                    result += s[i]
        return result