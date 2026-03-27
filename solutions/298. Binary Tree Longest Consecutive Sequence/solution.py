# Problem: Binary Tree Longest Consecutive Sequence
# Language: python3
# Runtime: 233 ms
# Memory: 28.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.x = 0
        
        @cache
        def dp(node):
            if node:
                ans = 1
                c1 = dp(node.left)
                c2 = dp(node.right)
                
                if node.left and node.left.val == node.val + 1:
                    ans = max(ans, c1 + 1)
                
                if node.right and node.right.val  == node.val + 1:
                    ans = max(ans, c2 + 1)
                
                self.x = max(self.x, ans)
                return ans
            else:
                return 0
        
        dp(root)
        return self.x