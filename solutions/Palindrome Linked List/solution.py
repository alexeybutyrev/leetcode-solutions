# Problem: Palindrome Linked List
# Language: python3
# Runtime: 578 ms
# Memory: 41.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        N = 0
        while p:
            N += 1
            p = p.next
        
        if N <= 1:
            return True
        
        fast = head
        for _ in range(N//2):
            fast = fast.next
        
        def rev(node):
            curr = None
            while node:
                n = node.next
                node.next = curr
                curr = node
                node = n
            return curr
        
        fast = rev(fast)
        
        slow = head
        for _ in range(N//2):
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
        
        