# Problem: Two Sum IV - Input is a BST
# Language: python3
# Runtime: 97 ms
# Memory: 21.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        self.ans = False
        def walk(node):
            if node:
                if k - node.val in s:
                    self.ans = True
                s.add(node.val)
                walk(node.left)
                walk(node.right)
        
        walk(root)
        return self.ans