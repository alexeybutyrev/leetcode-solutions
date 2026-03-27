# Problem: Remove Linked List Elements
# Language: python3
# Runtime: 64 ms
# Memory: 17.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h = ListNode(-1)
        r = h
        while head and head.val == val:
            head = head.next
        
        r = head
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
        return r
            