# Problem: Linked List Cycle
# Language: python3
# Runtime: 51 ms
# Memory: 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next or not head.next.next:
            return False
        
        slow = head.next
        fast = head.next.next
        
        
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        return slow == fast