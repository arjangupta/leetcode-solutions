# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Solved date: 2023-08-23

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LvlNumTreeNode:
    def __init__(self, tree_node: TreeNode, parent):
        self.tree_node = tree_node
        self.parent = parent
        if parent is None:
            self.level_num = 0
        else:
            self.level_num = parent.level_num + 1

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # Convert root to level order node and put it in visited and queue
        level_root = LvlNumTreeNode(root, None)
        visited:   List[LvlNumTreeNode] = [level_root]
        bfs_queue: List[LvlNumTreeNode] = [level_root]

        while len(bfs_queue) > 0:
            node = bfs_queue.pop(0)
            if node.tree_node.left is not None:
                level_left = LvlNumTreeNode(node.tree_node.left, node)
                visited.append(level_left)
                bfs_queue.append(level_left)
            if node.tree_node.right is not None:
                level_right = LvlNumTreeNode(node.tree_node.right, node)
                visited.append(level_right)
                bfs_queue.append(level_right)
        answer: List[List[int]] = []
        for lvlnode in visited:
            # print(f'({lvlnode.tree_node.val},{lvlnode.level_num})', end=' ')
            if lvlnode.level_num >= len(answer):
                answer.append([lvlnode.tree_node.val])
            else:
                answer[lvlnode.level_num].append(lvlnode.tree_node.val)
        return answer