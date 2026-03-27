# Problem: Find the Minimum and Maximum Number of Nodes Between Critical Points
# Language: python3
# Runtime: 920 ms
# Memory: 55 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        before = head.val
        n = head.next
        i = 1
        start = 0
        ind_before = 0
        mi = inf
        mx = 0
        while n:
            if n.next and (before < n.val > n.next.val or before > n.val < n.next.val):
                if not start:
                    start = i
                else:
                    mi = min(mi, i - ind_before)
                    mx = i - start
                ind_before = i
                    
            before = n.val
            n = n.next
            i+=1
        
        if mi != inf:
            return [mi, mx]
        return [-1,-1]
        
        