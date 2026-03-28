# Problem: Clone Graph
# Language: python
# Runtime: 40 ms
# Memory: 13.2 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        visited = dict()        
        visited[node] = Node(node.val,[])
        
        q = deque()
        q.append(node)
        
        while q:
            
            n = q.popleft()
            
            for nbr in n.neighbors:
                if nbr not in visited:
                    visited[nbr] = Node(nbr.val,[])
                    q.append(nbr)
                
                visited[n].neighbors.append(visited[nbr])
        
        return visited[node]