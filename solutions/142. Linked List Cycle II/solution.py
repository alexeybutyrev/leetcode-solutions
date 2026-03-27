# Problem: Linked List Cycle II
# Language: python3
# Runtime: 44 ms
# Memory: 18.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        
        p = 0
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None