# Problem: Range Sum of BST
# Language: python3
# Runtime: 256 ms
# Memory: 22.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def walk(node):
            if node:
                if node.val <= high and node.val >= low:
                    self.ans += node.val
                walk(node.left)
                walk(node.right)
        
        walk(root)
        return self.ans
            