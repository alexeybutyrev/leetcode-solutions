# Problem: Invert Binary Tree
# Language: python3
# Runtime: 28 ms
# Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        node = root
        def walk(node):
            if node:
                node.left, node.right = node.right, node.left
                walk(node.left)
                walk(node.right)
        
        walk(root)
        return node
    
        
        
            