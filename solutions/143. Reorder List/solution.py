# Problem: Reorder List
# Language: python3
# Runtime: 96 ms
# Memory: 23.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find half
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
                
        # reverse
        prev = None
        
        curr = slow
        
        while curr:
            next = curr.next
            prev,curr = curr,prev
            prev.next = curr
            curr = next
        
        
        # merge
        curr = head
        r = head
        while curr and prev and curr.next and prev.next:
            c = curr.next
            p = prev.next
            curr.next = prev
            prev.next = c
            prev = p
            curr = c
        return r