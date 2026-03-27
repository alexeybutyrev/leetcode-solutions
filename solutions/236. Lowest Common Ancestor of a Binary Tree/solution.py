# Problem: Lowest Common Ancestor of a Binary Tree
# Language: python3
# Runtime: 64 ms
# Memory: 27.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        
        def cs(node):
            nonlocal ans
            if node == p or node == q:
                return True
                
            if node:
                L = cs(node.left)
                R = cs(node.right)
                if L and R:
                    ans = node
                return L | R
            else:
                return False
        
        ans = None
        cs(root)
        if ans is None:
            return p if (cs(p.left) or cs(p.right)) else q
        return ans