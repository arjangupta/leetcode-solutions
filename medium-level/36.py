# https://leetcode.com/problems/valid-sudoku/
# Solved: 2023-08-28

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dicts = [{} for i in range(9)]
        row_dicts = [{} for i in range(9)]
        box_dicts = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == ".":
                    continue
                else:
                    if curr in row_dicts[i]:
                        if [i,j] != row_dicts[i][curr]:
                            print(f'row_dicts, {i},{curr}: [{i},{j}] != {row_dicts[i][curr]}')
                            return False
                    else:
                        row_dicts[i][curr] = [i,j]
                    if curr in col_dicts[j]:
                        if [i,j] != col_dicts[j][curr]:
                            print(f'col_dicts, {j}, {curr}: [{i},{j}] != {col_dicts[j][curr]}')
                            return False
                    else:
                        col_dicts[j][curr] = [i,j]
                    # Determine sub-box number
                    box_num = 0
                    for step in [0, 3, 6]:
                        if i < 3 + step:
                            if j < 3:
                                box_num = 0 + step
                                break
                            elif j < 6:
                                box_num = 1 + step
                                break
                            elif j < 9:
                                box_num = 2 + step
                                break
                    if curr in box_dicts[box_num]:
                        if [i,j] != box_dicts[box_num][curr]:
                            print(f'box_dicts, {box_num}, {curr}: [{i},{j}] != {box_dicts[box_num][curr]}')
                            return False
                    else:
                        box_dicts[box_num][curr] = [i,j]
        return True
