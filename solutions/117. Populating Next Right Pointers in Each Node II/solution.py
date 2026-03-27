# Problem: Populating Next Right Pointers in Each Node II
# Language: python3
# Runtime: 60 ms
# Memory: 15.4 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            L = len(q)
            
            before = None
            for i in range(L):
                node = q.popleft()
                if before is not None:
                    before.next = node
                
                before = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return root