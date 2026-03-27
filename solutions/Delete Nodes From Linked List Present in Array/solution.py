# Problem: Delete Nodes From Linked List Present in Array
# Language: python3
# Runtime: 147 ms
# Memory: 67.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)

        A = []

        while head:
            if head.val not in s:
                A.append(head.val)
            head = head.next
        
        p = ans = ListNode()

        for x in A:
            ans.next = ListNode(x)
            ans = ans.next
        return p.next