# Problem: Diameter of Binary Tree
# Language: python3
# Runtime: 44 ms
# Memory: 16.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = -1
        
        def walk(node):
            nonlocal ans
            if node:
                ll = 1 + walk(node.left)  if node.left  else 0
                rr = 1 + walk(node.right) if node.right else 0
                ans = max(ans, ll + rr)
                return max(ll, rr)
            else:
                return 0
            
        walk(root)
        return ans