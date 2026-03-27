# Problem: Merge In Between Linked Lists
# Language: python3
# Runtime: 564 ms
# Memory: 20 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = list1
        start = list1
        i = 0
        while i <= b:
            list1 = list1.next
            i+=1
        
        end = list1
        
        i = 0
        while i < a-1:
            start = start.next
            i+=1
        
        while list2:
            start.next = list2
            list2 = list2.next
            start = start.next
        
        start.next = end
        
        return res