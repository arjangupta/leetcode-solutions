from typing import List

class MinObject:
    def __init__(self, arr):
        self.min_indices = arr
        self.shared_count = 0

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ds: List[MinObject] = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val < self.getMin():
            self.min_ds.append(MinObject([len(self.stack)]))
        elif val == self.getMin():
            self.min_ds[-1].min_indices.append(len(self.stack))
            self.min_ds[-1].shared_count += 1
        else:
            self.min_ds[-1].shared_count += 1
        self.stack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if self.min_ds[-1].shared_count > 0:
            self.min_ds[-1].shared_count -= 1
            if removed == self.stack[self.min_ds[-1].min_indices[0]]:
                self.min_ds[-1].min_indices.pop()
        else:
            self.min_ds.pop()
        return removed

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        idx = self.min_ds[-1].min_indices[0]
        return self.stack[idx]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()