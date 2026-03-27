# Problem: Maximum Depth of Binary Tree
# Language: python3
# Runtime: 45 ms
# Memory: 16.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def walk(node, depth):
            nonlocal ans
            if not node:
                ans = max(ans, depth)
            else:
                walk(node.left, depth + 1)
                walk(node.right, depth + 1)
        
        walk(root, 0)
        return ans