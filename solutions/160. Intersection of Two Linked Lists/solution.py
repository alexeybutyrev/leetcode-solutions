# Problem: Intersection of Two Linked Lists
# Language: python3
# Runtime: 172 ms
# Memory: 29.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # reverse A

        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA
            
        
        