# Problem: Sum of Left Leaves
# Language: python3
# Runtime: 36 ms
# Memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def walk(node,d):
            if node:
                if d == 'l' and not node.left and not node.right: self.ans += node.val
                walk(node.left, 'l')
                walk(node.right, 'r')
        walk(root, 'n')
        return self.ans
            
            