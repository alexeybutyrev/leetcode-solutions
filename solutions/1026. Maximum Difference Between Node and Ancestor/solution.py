# Problem: Maximum Difference Between Node and Ancestor
# Language: python3
# Runtime: 30 ms
# Memory: 20.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def walk(node, mn, mx):
            if node:
                mn = min(mn, node.val)
                mx = max(mx, node.val)
                self.ans = max(abs(mx-mn), self.ans)
                
                walk(node.left, mn, mx)
                walk(node.right, mn, mx)
        
        walk(root, inf,-inf)
        
        return self.ans