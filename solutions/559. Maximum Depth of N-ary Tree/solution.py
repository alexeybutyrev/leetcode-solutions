# Problem: Maximum Depth of N-ary Tree
# Language: python3
# Runtime: 48 ms
# Memory: 16.1 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        q = deque([root])
        
        count = 0
        while q:
            count += 1
            L = len(q)
            for _ in range(L):
                node = q.popleft()
                for c in node.children:
                    q.append(c)
    
        return count