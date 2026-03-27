# Problem: Same Tree
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def walk(p,q):
            if not p and not q: return True
            if p and not q: return False
            if q and not p: return False
            if p.val != q.val: return False
            return walk(p.left, q.left) and walk(p.right, q.right)
        return walk(p,q) 