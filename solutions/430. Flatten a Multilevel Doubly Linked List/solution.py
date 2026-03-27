# Problem: Flatten a Multilevel Doubly Linked List
# Language: python3
# Runtime: 36 ms
# Memory: 15.4 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        ans = Node(-1,None, None,None)
        A = ans
        def flatten(node):
            if node:
                nonlocal ans
                ans.next = Node(node.val,None, None, None)
                b = ans
                ans = ans.next
                ans.prev = b
                if node.child:
                    flatten(node.child)
                flatten(node.next)
            
                    
        
        flatten(head)
        A = A.next
        A.prev = None
        return A