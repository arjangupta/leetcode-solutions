# https://leetcode.com/problems/equal-row-and-column-pairs/
# Solved: 2023-08-26

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hashes = [hash(str(r)) for r in grid]
        cols = []
        for r in grid:
            cols.append([])
        for r in grid:
            for i in range(len(grid)):
                cols[i].append(r[i])
        print(cols)
        col_hashes = [hash(str(c)) for c in cols]
        matches = 0
        for col_hash in col_hashes:
            for row_hash in row_hashes:
                if col_hash == row_hash:
                    matches += 1
        return matches