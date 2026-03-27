# Problem: Diameter of Binary Tree
# Language: python3
# Runtime: 47 ms
# Memory: 17.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0        
        def walk(node):
            nonlocal ans
            if not node:
                return 0
            l = walk(node.left)
            r = walk(node.right)
            ans = max(ans, l + r)
            return 1 + max(l,r)
        
        walk(root)
        return ans