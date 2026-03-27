# Problem: Validate Binary Search Tree
# Language: python3
# Runtime: 35 ms
# Memory: 18.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def walk(node, lo, hi):
            if node:
                if lo < node.val < hi:
                    return walk(node.left, lo, node.val) and walk(node.right, node.val, hi)
                return False
                
            return True
        
        return walk(root, -inf, inf)