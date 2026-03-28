# Problem: Lowest Common Ancestor of a Binary Tree II
# Language: python3
# Runtime: 380 ms
# Memory: 29 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find_node(node, N):
            nonlocal ans
            if node == N:
                return True
            if node:
                L = find_node(node.left,  N)
                R = find_node(node.right, N)
                if L and R:
                    ans = node
                return L or R
            else:
                return False
        
        if not find_node(root, p) or not find_node(root,q):
            return None
        
        def cs(node):
            nonlocal ans
            if node == p or node == q:
                return True
            if node:
                L = cs(node.left)
                R = cs(node.right)
                if L and R:
                    ans = node
                return L or R
            else:
                return False
        
        ans = None
        cs(root)
        if ans is not None:
            return ans
        
        if cs(p.left) or cs(p.right):
            return p
        else:
            return q
        