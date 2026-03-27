# Problem: Reverse Linked List II
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        
        curr, prev = head, None
        
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        
        # reverse
        
        p = None
        c = curr
        
        before = prev
        after = curr
        
        while right:
            n = c.next
            c.next, p, c = p, c, n
            right -= 1
        
        if before:
            before.next = p
        else:
            head = p
            
        after.next = n
        return head
            