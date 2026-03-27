# Problem: Middle of the Linked List
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        return slow
            