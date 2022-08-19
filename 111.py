# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         if not root.left:
#             return self.minDepth(root.right) + 1
#         if not root.right:
#             return self.minDepth(root.left) + 1
#         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        depth = 0
        while stack:
            depth += 1
            for _ in range(len(stack)):
                node = stack.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return depth
