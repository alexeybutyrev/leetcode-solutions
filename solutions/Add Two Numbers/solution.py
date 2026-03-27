# Problem: Add Two Numbers
# Language: python3
# Runtime: 56 ms
# Memory: 14.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        
        L = ListNode(-1)
        LL = L
        left = 0
        while l1 and l2:
            v = left + l1.val + l2.val
            
            if v%10 != v:
                left = 1
                L.next = ListNode(v % 10)
            else:
                L.next = ListNode(v)
                left = 0
                
            L = L.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            v = left + l1.val
            
            if v%10 != v:
                left = 1
                L.next = ListNode(v % 10)
            else:
                L.next = ListNode(v)
                left = 0
                
            L = L.next
            
            l1 = l1.next
        
        while l2:
            v = left + l2.val
            
            if v%10 != v:
                left = 1
                L.next = ListNode(v % 10)
            else:
                L.next = ListNode(v)
                left = 0
                
            L = L.next
            
            l2 = l2.next
        
        if left:
            L.next = ListNode(left)
            
        
        return LL.next