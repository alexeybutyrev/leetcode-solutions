# Problem: Find Largest Value in Each Tree Row
# Language: python3
# Runtime: 48 ms
# Memory: 16.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        q = deque([root])
        
        res = []
        while q:
            l = len(q)
            mx = -inf
            for _ in range(l):
                node = q.popleft()
                mx = max(node.val, mx)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(mx)
        
        return res