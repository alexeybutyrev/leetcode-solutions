# Problem: Balance a Binary Search Tree
# Language: python3
# Runtime: 27 ms
# Memory: 26.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        A = []
        def walk(node):
            if node:
                walk(node.left)
                A.append(node.val)
                walk(node.right)
        
        walk(root)
        def build(A):
            if not A: return None
            if len(A) == 1: return TreeNode(A[0])
            
            N = len(A)
            mid = N // 2
            t = TreeNode(A[mid])
            t.left = build(A[0:mid])
            t.right = build(A[mid+1:])
            return t

        return build(A)
            
                
                    