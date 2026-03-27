# Problem: Swapping Nodes in a Linked List
# Language: python3
# Runtime: 921 ms
# Memory: 50.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        A = []
        
        p = head
        N = 0
        while p:
            N += 1
            p = p.next
            
        p = head
        for _ in range(k-1):
            p = p.next

        A.append(p)
        
        v = head
        for _ in range(N - k):
            v = v.next
        

        A.append(v)
        
        A[0].val,A[1].val = A[1].val, A[0].val
        return head
        