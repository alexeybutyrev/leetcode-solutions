# Problem: Remove Duplicates From an Unsorted Linked List
# Language: python3
# Runtime: 1875 ms
# Memory: 55.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        ans = p = ListNode()
        h = head
        c = Counter()
        while h:
            c[h.val]+=1
            h = h.next
        
        
        while head:
            if c[head.val] == 1:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return ans.next