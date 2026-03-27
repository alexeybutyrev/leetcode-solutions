# Problem: Partition List
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        L = ListNode(-1)
        R = ListNode(-1)
        LL = L
        RR = R
        while head:
            if head.val < x:
                L.next = ListNode(head.val)
                L = L.next
            else:
                R.next = ListNode(head.val)
                R = R.next

            head = head.next
        
        L.next = RR.next
        return LL.next
        