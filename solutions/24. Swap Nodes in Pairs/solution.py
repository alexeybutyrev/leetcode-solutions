# Problem: Swap Nodes in Pairs
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = head
        ce = ListNode(1)
        co = ListNode(1)
        odd  = co
        even = ce
        while head and head.next:
            ce.next = head
            co.next = head.next
            head = head.next.next
            co = co.next
            ce = ce.next
        
        if head:
            ce.next = head
            ce = ce.next
        ce.next = None
        co.next = None
        
        odd = odd.next
        even = even.next
        
        h = ListNode(1)
        hh = h
        while odd and even:
            h.next = ListNode(odd.val)
            h = h.next
            h.next = ListNode(even.val)
            h = h.next
            odd = odd.next
            even = even.next
        
        if even:
            h.next = ListNode(even.val)
        if odd:
            h.next = ListNode(odd.val)    
        return hh.next
        