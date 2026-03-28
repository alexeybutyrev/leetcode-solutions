# Problem: Lowest Common Ancestor of a Binary Search Tree
# Language: python3
# Runtime: 68 ms
# Memory: 18.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        P = p.val
        Q = q.val
        def cs(node):
            if P > node.val and Q > node.val:
                return cs(node.right)
            elif P < node.val and Q < node.val:
                return cs(node.left)
            else:
                return node
            
        
        return cs(root)