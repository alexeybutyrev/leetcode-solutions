# Problem: Delete the Middle Node of a Linked List
# Language: python3
# Runtime: 4122 ms
# Memory: 77.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        
        l = ListNode(-1)
        ans = l
        for i in range(len(A)):
            if i != (len(A) // 2):
                l.next = ListNode(A[i])
                l = l.next
        
        return ans.next