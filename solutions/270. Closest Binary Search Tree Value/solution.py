# Problem: Closest Binary Search Tree Value
# Language: python3
# Runtime: 44 ms
# Memory: 15.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        result = root.val
        delta = abs(root.val - target)
        
        def walk(root):
            nonlocal result
            nonlocal delta

#            if root.left and root.right:
#                if abs(root.left.val - target) < delta:
#                    if abs(root.right.val - target) < abs(root.left.val - target):
                        
            
            if root.left and abs(root.left.val - target) < delta:
                result = root.left.val
                delta = abs(root.left.val - target)
            
            if root.right and abs(root.right.val - target) < delta:
                result = root.right.val
                delta = abs(root.right.val - target)
                
            if target > root.val:
                if root.right:
                    walk(root.right)
            else:
                if root.left:
                    walk(root.left)
        
        walk(root)
        
        return result
        