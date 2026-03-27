# Problem: Remove Duplicates from Sorted List II
# Language: python3
# Runtime: 40 ms
# Memory: 14.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(-1)
        ans = res
        
        while head:
            while head and head.next and head.val == head.next.val:
                v = head.val
                while head and head.val == v:
                    head = head.next
            
            res.next = head
            res = res.next
            if head:
                head = head.next
            
            
        return ans.next