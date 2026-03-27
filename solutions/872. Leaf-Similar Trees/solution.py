# Problem: Leaf-Similar Trees
# Language: python3
# Runtime: 39 ms
# Memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def walk(node, A):
            if node:
                if not node.left and not node.right:
                    A.append(node.val)
                walk(node.left, A)
                walk(node.right, A)
        A = []
        B = []
        walk(root1,A)
        walk(root2,B)
        return A == B
                