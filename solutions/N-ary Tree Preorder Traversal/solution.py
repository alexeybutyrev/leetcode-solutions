# Problem: N-ary Tree Preorder Traversal
# Language: python3
# Runtime: 52 ms
# Memory: 16.1 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def walk(node):
            if node:
                arr.append(node.val)
                for c in node.children:
                    walk(c)
        
        walk(root)
        return arr
                    