# Problem: Diameter of N-Ary Tree
# Language: python3
# Runtime: 107 ms
# Memory: 16 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        def walk(node):
            
            if node:
                A = []
                for c in node.children:
                    A.append(1 + walk(c))
                
                self.ans = max(self.ans, max(A) if A else 0)
                if len(A) > 1:
                    A.sort()
                    self.ans = max(self.ans, A[-1] + A[-2])
                return max(A) if A else 0
            else:
                return 0
    
        walk(root)
        return self.ans