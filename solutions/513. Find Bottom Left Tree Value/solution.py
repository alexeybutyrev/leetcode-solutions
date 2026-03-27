# Problem: Find Bottom Left Tree Value
# Language: python3
# Runtime: 48 ms
# Memory: 18.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        glevel = 0
        res = root.val
        
        def walk(root,level):
            nonlocal res
            nonlocal glevel
            if root:
                if root.left:
                    if glevel < level:
                        glevel = level
                        res = root.left.val
                    walk(root.left, level + 1)
                if root.right:
                    if glevel < level:
                        glevel = level
                        res = root.right.val
                    walk(root.right, level + 1)
                    
        
        
        walk(root, 1)
        return res
    