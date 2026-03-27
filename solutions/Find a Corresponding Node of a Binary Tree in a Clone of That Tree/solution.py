# Problem: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Language: python3
# Runtime: 648 ms
# Memory: 24 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        res = None
        def walk(no, nc):
            nonlocal res
            if no == target:
                res = nc
            if no:
                walk(no.left, nc.left)
                walk(no.right, nc.right)
        
        walk(original, cloned)
        return res