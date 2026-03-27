# Problem: Inorder Successor in BST II
# Language: python3
# Runtime: 90 ms
# Memory: 22.1 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        val = node.val
        while node.parent:
            node = node.parent
        
        hm = {}
        A = []
        def walk(node):
            if node:
                walk(node.left)
                A.append(node.val)
                hm[node.val] = node
                walk(node.right)
        
        
        walk(node)
        ind = bisect_right(A,val)
        if ind == len(A):
            return None
        return hm[A[ind]]
        