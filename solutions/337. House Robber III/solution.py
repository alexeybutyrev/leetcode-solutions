# Problem: House Robber III
# Language: python3
# Runtime: 40 ms
# Memory: 16.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rob(self, root: TreeNode) -> int:

        def walk(node):
            if not node:
                return (0,0)
            
            left  = walk(node.left)
            right = walk(node.right)
            
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob,not_rob)
        
        return max(walk(root))
    
    