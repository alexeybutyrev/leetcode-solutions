# Problem: Delete the Middle Node of a Linked List
# Language: python3
# Runtime: 1908 ms
# Memory: 60.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        N = 0
        p = head
        while p:
            N += 1
            p = p.next
        if N == 0 or N == 1:
            return None
        
        p = head
        for i in range(N//2-1):
            p = p.next
            
        p.next = p.next.next
        
        return head