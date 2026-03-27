# Problem: Even Odd Tree
# Language: python3
# Runtime: 214 ms
# Memory: 37.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        q = deque()
        q.append(root)
        
        odd = True
        while q:
            l = len(q)
            values = []
            for _ in range(l):
                node = q.popleft()
                if (odd and node.val % 2 == 0) or (not odd and node.val % 2 != 0):
                    return False
                values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if values:
                for i in range(1,len(values)):
                    if odd and values[i] <= values[i-1] or not odd and values[i] >= values[i-1]:
                        return False
            odd = not odd
        
        return True