# Problem: Reverse Linked List
# Language: python
# Runtime: 28 ms
# Memory: 17.3 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        p = self._reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    def reverseList(self, head):
        if not head:
            return head
        return self._reverseList(head)