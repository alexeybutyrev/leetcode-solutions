# Problem: Merge Two Sorted Lists
# Language: python
# Runtime: 20 ms
# Memory: 13.6 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L = ListNode(-1)
        LL = L
        while l1 and l2:
            if l1.val < l2.val:
                L.next = l1
                l1 = l1.next
            else:
                L.next = l2
                l2 = l2.next
            L = L.next
        if l2:
            L.next = l2
        if l1:
            L.next = l1
            
        return LL.next
            