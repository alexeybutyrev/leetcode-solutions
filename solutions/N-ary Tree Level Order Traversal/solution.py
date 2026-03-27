# Problem: N-ary Tree Level Order Traversal
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        
        q = deque([root])
        ans = []
        while q:
            L = len(q)
            l = []
            for _ in range(L):
                node = q.popleft()
                l.append(node.val)
                for c in node.children:
                    q.append(c)
            ans.append(l)
        return ans