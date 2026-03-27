# Problem: Convert Binary Search Tree to Sorted Doubly Linked List
# Language: python3
# Runtime: 32 ms
# Memory: 15.6 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        A = []
        
        def walk(node):
            if node:
                walk(node.left)
                A.append(node)
                walk(node.right)
        
        
        walk(root)
        
        N = len(A)
        if N == 1:
            A[0].left = A[0]
            A[0].right = A[0]
            return A[0]
        A[0].left = A[N-1]
        A[0].right = A[1]
        
        A[N-1].left = A[N-2]
        A[N-1].right = A[0]
        for i in range(1, len(A)-1):
            A[i].right = A[i+1]
            A[i].left  = A[i-1]
        
        return A[0]