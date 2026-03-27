# Problem: Sum of Nodes with Even-Valued Grandparent
# Language: python3
# Runtime: 116 ms
# Memory: 17.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = [(root,False, False)]
        sm = 0
        while q:
            l = len(q)
            for _ in range(l):
                n, par, gpar = q.pop(0)
                if gpar:
                    sm += n.val
                if n.left:
                    q.append((n.left,n.val % 2 == 0, par))
                    
                if n.right:
                    q.append((n.right,n.val % 2 == 0, par))
        
        return sm
                