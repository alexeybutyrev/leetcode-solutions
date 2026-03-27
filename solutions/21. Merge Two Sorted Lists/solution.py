# Problem: Merge Two Sorted Lists
# Language: python3
# Runtime: 36 ms
# Memory: 14.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        v = res
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
                res = res.next
            else:
                res.next = l2
                l2 = l2.next
                res = res.next
        
        if l1:
            while l1:
                res.next = l1
                l1 = l1.next
                res = res.next
        if l2:
            while l2:
                res.next = l2
                l2 = l2.next
                res = res.next
            
            
        return v.next