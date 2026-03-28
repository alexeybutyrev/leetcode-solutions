# Problem: Sum Root to Leaf Numbers
# Language: python3
# Runtime: 32 ms
# Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sum_ = 0
        q = deque([(root, "")])
        
        while q:
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                if not n[0].left and not n[0].right:
                    sum_ += int(n[1] + str(n[0].val))
                if n[0].left:
                    q.append((n[0].left, n[1] + str(n[0].val)))
                
                if n[0].right:
                    q.append((n[0].right, n[1] + str(n[0].val)))
                
                
        
        return sum_
        