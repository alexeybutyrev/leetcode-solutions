# Problem: Find Root of N-Ary Tree
# Language: python3
# Runtime: 200 ms
# Memory: 36.1 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        vals = set(map(lambda x: x.val, tree))
        visited = set()
        
        def walk(root):
            if root and root.val not in visited:
                visited.add(root.val)
                for c in root.children:
                    walk(c)
        
        for n in tree:
            for c in n.children:
                if c and c.val not in visited:
                    walk(c)
        
        for n in tree:
            if n.val not in visited:
                return n
        