# Problem: Maximum Twin Sum of a Linked List
# Language: python3
# Runtime: 908 ms
# Memory: 56.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A  = []
        while head:
            A.append(head.val)
            head = head.next
        ans = 0
        N = len(A)
        for i in range(N//2):
            ans = max(ans, A[i] + A[N - i - 1])
        
        return ans