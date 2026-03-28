# Problem: Vertical Order Traversal of a Binary Tree
# Language: python3
# Runtime: 32 ms
# Memory: 14.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        hm = defaultdict(list)
        def walk(node, x, y):
            if node:
                hm[x].append( (-y,node.val))
                walk(node.left, x - 1, y - 1)
                walk(node.right, x + 1, y - 1)
        
        walk(root,0,0)
        res = []
        
        for k in sorted(hm.keys()):
            l = map( lambda x: x[1], list(sorted(hm[k]) )) 
            res.append( l)
        
        return res