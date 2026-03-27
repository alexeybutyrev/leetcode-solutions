# Problem: Sum of Root To Leaf Binary Numbers
# Language: python3
# Runtime: 0 ms
# Memory: 19.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def walk(node,c):
            
            if not node.left and not node.right:
                return c
            cl = walk(node.left,  (c << 1) + node.left.val)  if node.left else 0
            cr = walk(node.right, (c << 1) + node.right.val) if node.right else 0
            return cl + cr

        return walk(root, root.val)
                    
                    
            
            