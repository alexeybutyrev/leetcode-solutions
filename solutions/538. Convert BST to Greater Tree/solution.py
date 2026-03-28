# Problem: Convert BST to Greater Tree
# Language: python3
# Runtime: 88 ms
# Memory: 17.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        res = []
        
        def walk(node):
            if node:
                walk(node.left)
                res.append(node.val)
                walk(node.right)
                
        
        walk(root)
        
        for i in range(len(res)-2, -1, -1):
            res[i] += res[i+1]
        
        i = 0
        def fix(node):
            nonlocal i
            if node:
                fix(node.left)
                node.val = res[i]
                i+=1
                fix(node.right)

        fix(root)
        return root