# Problem: Convert Sorted Array to Binary Search Tree
# Language: python3
# Runtime: 109 ms
# Memory: 15.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, A: List[int]) -> Optional[TreeNode]:
        
        def walk(A):
            
            if len(A) == 1:
                return TreeNode(A[0])
            if len(A) == 0:
                return None
            x = len(A) // 2
            ans = TreeNode(A[x])
            ans.left = walk(A[:x])
            ans.right = walk(A[x+1:])
            return ans
        return walk(A)