# Problem: Binary Tree Tilt
# Language: python3
# Runtime: 560 ms
# Memory: 16.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        def find_sum(root):
            if root:
                return root.val + find_sum(root.left) + find_sum(root.right)
            else:
                return 0
        
        def tilt(root):
            if root:
                return abs(find_sum(root.left) - find_sum(root.right)) + tilt(root.left) + tilt(root.right)
            else:
                return 0
                
        
        return tilt(root)
        