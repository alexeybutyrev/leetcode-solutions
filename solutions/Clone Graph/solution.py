# Problem: Clone Graph
# Language: python3
# Runtime: 35 ms
# Memory: 14.3 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = defaultdict(set)
        def clone(node):
            if not node: return None
            if node not in hm:
                hm[node] = Node(node.val)
                for nb in node.neighbors:
                    c = clone(nb)
                    hm[node].neighbors.append(c)
        
            return hm[node]
        n = clone(node)
        return n
            