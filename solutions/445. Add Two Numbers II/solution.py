# Problem: Add Two Numbers II
# Language: python3
# Runtime: 60 ms
# Memory: 14.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse ll 
        
        if not l1 and l2:
            return l1
        
        def reverse(head):
            prev = None
            while head:
                curr = head.next
                head.next = prev
                prev = head
                head = curr
            return prev
        
        def ln(l):
            count = 0
            while l:
                l = l.next
                count += 1
            return count
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        n1,n2 = ln(l1), ln(l2)
                
            
        if n2 > n1:
            l1,l2 = l2,l1
        
        rest = 0
        res = l1
        while l1:
            v = l1.val + rest
            if l2:
                v += l2.val
                l2 = l2.next
            l1.val = v %10
            rest = v // 10
            l1 = l1.next
        #print(res,rest)
        if rest:
            res = reverse(res)
            head = ListNode(rest)
            head.next = res
        else:
            head = reverse(res)
        #print(res,rest)
        return head
        