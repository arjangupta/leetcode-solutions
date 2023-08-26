# https://leetcode.com/problems/delete-node-in-a-bst/
# Unsolved - 81/92 test cases passed
# Attempted - 2023-08-24
# Difficulty: Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class UpTreeNode:
    def __init__(self, node: TreeNode, parent: Optional[TreeNode], is_left_child: Optional[bool]):
        self.node = node
        self.parent = parent
        self.is_left_child = is_left_child

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        original_root = root
        dfs_stack: List[UpTreeNode] = [UpTreeNode(root, None, None)]
        traverse = True
        curr = None
        found = False
        while traverse:
            curr = dfs_stack.pop()
            if curr.node.val == key:
                traverse = False
                found = True
                break
            if curr.node.left is not None:
                dfs_stack.append(UpTreeNode(curr.node.left, curr.node, True))
            if curr.node.right is not None:
                dfs_stack.append(UpTreeNode(curr.node.right, curr.node, False))
            if len(dfs_stack) == 0:
                traverse = False
                found = False
        if not found:
            print("Not found")
            return original_root
        elif curr.node is original_root:
            new_root = None
            if original_root.right is not None:
                new_root = original_root.right
            else:
                new_root = original_root.left
                return new_root
            if new_root is not None:
                to_be_reattached = new_root.left
                new_root.left = original_root.left
                if to_be_reattached is not None:
                    find_attach = new_root.left
                    while find_attach.right is not None:
                        find_attach = find_attach.right
                    find_attach.right = to_be_reattached
            return new_root
        else: # Node to be replaced is not the original root.
            if curr.is_left_child:
                replacement = curr.node.right
                if replacement is None:
                    curr.parent.left = curr.node.left
                    return original_root
                curr.parent.left = replacement
                to_be_reattached = replacement.left
                replacement.left = curr.node.left
                if replacement.right is None:
                    replacement.right = to_be_reattached
                else:
                    find_attach = replacement.right
                    while find_attach.left is not None:
                        find_attach = find_attach.left
                    find_attach.left = to_be_reattached
            else:
                replacement = curr.node.left
                if replacement is None:
                    curr.parent.right = curr.node.right
                    return original_root
                curr.parent.right = replacement
                to_be_reattached = replacement.right
                replacement.right = curr.node.right
                if replacement.left is None:
                    replacement.left = to_be_reattached
                else:
                    find_attach = replacement.left
                    while find_attach.right is not None:
                        find_attach = find_attach.right
                    find_attach.right = to_be_reattached
        return original_root