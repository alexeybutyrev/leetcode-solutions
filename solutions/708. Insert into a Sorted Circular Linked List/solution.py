# Problem: Insert into a Sorted Circular Linked List
# Language: python3
# Runtime: 36 ms
# Memory: 14.3 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        
        h = head
        hn = head.next
        
        max_node = h
        
        if head.val <= insertVal and insertVal  <= head.next.val:
            n = head.next
            head.next = Node(insertVal)
            head = head.next
            head.next = n
            return h
        
        head = head.next
        if max_node.val <= head.val:
            max_node = head
        
        while head != h:
            if head.val <= insertVal and insertVal  <= head.next.val:
                n = head.next
                head.next = Node(insertVal)
                head = head.next
                head.next = n
                return h
            head = head.next
            if max_node.val <= head.val:
                max_node = head
        

        n = max_node.next
        max_node.next = Node(insertVal)
        max_node = max_node.next
        max_node.next = n
        
        return h
            
            