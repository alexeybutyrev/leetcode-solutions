# Problem: Insertion Sort List
# Language: python3
# Runtime: 1484 ms
# Memory: 15.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        phead = ListNode()
        
        curr = head
        
        while curr:
            
            prev_node = phead
            next_node = prev_node.next
            
            while next_node:
                if next_node.val > curr.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            nn = curr.next
            curr.next = next_node
            prev_node.next = curr
            
            curr = nn
            
        return phead.next