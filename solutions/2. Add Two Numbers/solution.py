# Problem: Add Two Numbers
# Language: python3
# Runtime: 60 ms
# Memory: 16.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list
        
        def rev(head):
            a = None
            while head:
                n,head.next = head.next,a
                a,head = head, n
            return a
        
        #l1 = rev(l1)
        #l2 = rev(l2)
        
        rem = 0
        p = ans = ListNode(-1)
        while l1 or l2:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0
            curr = c1 + c2 + rem
            rem = curr // 10
            curr %= 10
            p.next = ListNode(curr)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if rem:
            p.next = ListNode(rem)
            
        return ans.next
        # walk head to tail
        