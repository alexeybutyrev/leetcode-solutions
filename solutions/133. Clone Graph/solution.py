# Problem: Clone Graph
# Language: python3
# Runtime: 41 ms
# Memory: 16.8 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hm = {}
        def clone(node):
            if node not in hm:
                hm[node] = Node(node.val)
                for c in node.neighbors:
                    hm[node].neighbors.append(clone(c))
            return hm[node]
        
        return clone(node)