# Problem: Rotate List
# Language: python3
# Runtime: 0 ms
# Memory: 17.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        N = 0
        h = head
        while h:
            N += 1
            h = h.next
        
        k %= N
        if not k: return head
        
        p0 = h = head
        for i in range(N-k-1):
            h = h.next
        
        ans = p = h.next
        h.next = None
        for _ in range(k-1):
            p = p.next
        
        p.next = p0
        
        return ans