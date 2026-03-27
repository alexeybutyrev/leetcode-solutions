# Problem: Evaluate Boolean Binary Tree
# Language: python3
# Runtime: 81 ms
# Memory: 14.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def walk(node):
            if node.val == 0: return False
            if node.val == 1: return True
            if node.val == 2: return walk(node.left) or walk(node.right)
            if node.val == 3: return walk(node.left) and walk(node.right)
        
        return walk(root)