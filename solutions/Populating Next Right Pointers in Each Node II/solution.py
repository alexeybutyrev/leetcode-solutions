# Problem: Populating Next Right Pointers in Each Node II
# Language: python3
# Runtime: 52 ms
# Memory: 15.5 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        res = Node(root.val)
        r = res
        
        q = deque([(root, res)])
        
        while q:
            l = len(q)
            res_before = None
            for _ in range(l):
                node, res = q.popleft()
                if res_before is not None:
                    res_before.next = res
                
                if node.left:
                    res.left = node.left
                    q.append((node.left, res.left))
                if node.right:
                    res.right = node.right
                    q.append((node.right, res.right))

                res_before = res
                
        return r