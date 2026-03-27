# Problem: Copy List with Random Pointer
# Language: python3
# Runtime: 32 ms
# Memory: 15.6 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        hm = {}
        def dfs(node):
            if node is None:
                return None
            
            if node in hm:
                return hm[node]
            
            n = Node(node.val)
            hm[node] = n
            
            n.next   = dfs(node.next)
            n.random = dfs(node.random)
            return n
        
        return dfs(head)