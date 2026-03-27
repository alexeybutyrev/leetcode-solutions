# Problem: Remove Nth Node From End of List
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        L = []
        while head:
            L.append(head)
            head = head.next
        
        if len(L) == n == 1:
            return None
        
        if n == 1:
            L[-n-1].next = None
            return L[0]
        
        if len(L) -n -1 >= 0:
            L[-n-1].next = L[-n+1]
            return L[0]
        
        if len(L) == n:
            return L[0].next
        
        
        return L[0]