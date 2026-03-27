# Problem: Binary Search Tree to Greater Sum Tree
# Language: python3
# Runtime: 30 ms
# Memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        mp = set()
        def col(node):
            if node:
                mp.add(node.val)
                col(node.left)
                col(node.right)
        
        def walk(node):
            if node:
                s = 0
                for x in mp:
                    if x>=node.val:
                        s+=x
                node.val = s
                
                walk(node.left)
                walk(node.right)
        col(root)
        
        walk(root)
        
        return root