# Problem: Reverse Linked List
# Language: python3
# Runtime: 32 ms
# Memory: 15.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            curr = head.next
            head.next = prev
            prev = head
            head = curr
            
            
            
            
        return prev
            
        
            