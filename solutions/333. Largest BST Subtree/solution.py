# Problem: Largest BST Subtree
# Language: python3
# Runtime: 85 ms
# Memory: 18.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node):
            if not node:
                return 0,0,inf,-inf
            N1, n1, min1, max1 = dp(node.left)
            N2, n2, min2, max2 = dp(node.right)
            if  max1 < node.val < min2:
                n = n1 + n2 + 1 
            else:
                n = -inf
            return max(N1,N2,n), n, min(min1,node.val), max(max2,node.val)
        return dp(root)[0]