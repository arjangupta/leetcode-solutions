# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Solved: 2023-09-14

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1 and tokens[0].isnumeric():
            return int(tokens[0])
        if len(tokens) < 3:
            return 0
        num_stack = []
        for c in tokens:
            if c.lstrip('-').isnumeric():
                num_stack.append(int(c))
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                if c == '/':
                    num_stack.append(int(a/b))
                elif c == '-':
                    num_stack.append(a-b)
                elif c == '+':
                    num_stack.append(a+b)
                else:
                    num_stack.append(a*b)
        return int(num_stack[0])