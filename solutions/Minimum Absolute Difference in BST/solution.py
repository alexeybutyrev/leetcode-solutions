# Problem: Minimum Absolute Difference in BST
# Language: python3
# Runtime: 58 ms
# Memory: 18.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        A = []
        def walk(node):
            if node:
                walk(node.left)
                A.append(node.val)
                walk(node.right)
            
        walk(root)
        ans = inf
        for i in range(1,len(A)):
            ans = min(ans,A[i] - A[i-1])
        return ans