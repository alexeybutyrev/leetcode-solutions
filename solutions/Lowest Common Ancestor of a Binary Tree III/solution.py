# Problem: Lowest Common Ancestor of a Binary Tree III
# Language: python3
# Runtime: 59 ms
# Memory: 20.9 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        
        while q:
            if q in seen: return q
            q = q.parent