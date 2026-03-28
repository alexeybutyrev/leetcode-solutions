# Problem: Merge Two Sorted Lists
# Language: python
# Runtime: 20 ms
# Memory: 12 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _m2l(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        if l1.val < l2.val:
            l1.next = self._m2l(l1.next,l2)
            return l1
        else:
            l2.next = self._m2l(l2.next,l1)
            return l2
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self._m2l(l1,l2)
            