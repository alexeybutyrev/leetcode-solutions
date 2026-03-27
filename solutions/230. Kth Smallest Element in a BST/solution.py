# Problem: Kth Smallest Element in a BST
# Language: python3
# Runtime: 47 ms
# Memory: 20.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = 0
        def walk(node):
            if node:
                walk(node.left)
                self.k-=1
                if not self.k:
                    self.ans = node.val
                walk(node.right)
        walk(root)
        return self.ans