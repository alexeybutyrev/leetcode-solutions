# Problem: Insert Greatest Common Divisors in Linked List
# Language: python3
# Runtime: 113 ms
# Memory: 21.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = [head.val]
        head = head.next
        while head:
            A.append(gcd(A[-1], head.val))
            A.append(head.val)
            head = head.next
            
        r = l = ListNode()
        for x in A:
            l.next = ListNode(x)
            l = l.next
        return r.next