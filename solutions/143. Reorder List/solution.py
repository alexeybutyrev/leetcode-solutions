# Problem: Reorder List
# Language: python3
# Runtime: 82 ms
# Memory: 26 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = ans = head
        
        q = deque()        
        while head:    
            q.append(head)
            head = head.next
        
        p = ans = ListNode(-1)
        while q:
            p.next = q.popleft()
            p = p.next
            if q:
                p.next = q.pop()
                p = p.next
                
        
        if p.next:
            p.next = None
        return ans
        
    
    