# Problem: Merge Nodes in Between Zeros
# Language: python3
# Runtime: 955 ms
# Memory: 75.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode(-1)
        ans = p
        s = 0
        while head:
            if head.val == 0 and s:
                p.next = ListNode(s)
                p = p.next
                s = 0
            else:
                s += head.val
            head = head.next
        
        return ans.next
            
                
            
            
        