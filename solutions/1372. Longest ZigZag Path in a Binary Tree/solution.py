# Problem: Longest ZigZag Path in a Binary Tree
# Language: python3
# Runtime: 520 ms
# Memory: 61.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def walk(node, d, s):
            if node:
                self.ans = max(self.ans, s)

                if d:
                    walk(node.left, False, s + 1)
                    walk(node.right, True, 1)
                else:
                    walk(node.left, False, 1)
                    walk(node.right, True, s + 1)

        

        
        walk(root, False,0)
        walk(root, True,0)
        return self.ans