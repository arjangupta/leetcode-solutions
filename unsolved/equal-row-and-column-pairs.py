# https://leetcode.com/problems/equal-row-and-column-pairs/
# Attempted: 2023-08-25
# Difficulty: Medium

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
        if row_hashes == col_hashes:
            matches = len(grid)
            first_e = cols[0][0]
            for e in cols[0]:
                if e != first_e:
                    return matches
            return matches*2
        row_matches = 0
        for h in row_hashes:
            if h in col_hashes:
                row_matches += 1
        col_matches = 0
        for h in col_hashes:
            if h in row_hashes:
                col_matches += 1
        return row_matches if row_matches > col_matches else col_matches