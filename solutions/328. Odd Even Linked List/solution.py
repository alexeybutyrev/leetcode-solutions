# Problem: Odd Even Linked List
# Language: python3
# Runtime: 40 ms
# Memory: 16.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        p0 = p1 = head
        p3 = p2 = head.next

        while p1 and p2 and p2.next:
            c = p2.next
            
            p1.next = c
            p1 = p1.next

            c2 = p2.next.next
            p2.next = c2
            p2 = p2.next
        
        p1.next = p3
        return p0
