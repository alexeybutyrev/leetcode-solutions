# Problem: Delete Node in a Linked List
# Language: python3
# Runtime: 40 ms
# Memory: 16.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if node.next:
                node.val = node.next.val
                if not node.next.next:
                    node.next = None
                
            node = node.next