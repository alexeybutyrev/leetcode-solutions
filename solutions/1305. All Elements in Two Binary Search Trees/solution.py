# Problem: All Elements in Two Binary Search Trees
# Language: python3
# Runtime: 352 ms
# Memory: 22.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        A = []
        def walk(node):
            if node:
                walk(node.left)
                A.append(node.val)
                walk(node.right)
        
        walk(root1)
        B = A[:]
        A = []
        walk(root2)
        
        C = []
        
        nA = len(A)
        nB = len(B)
        i = j = 0
        while i < nA and j < nB:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        
        if i == nA:
            C = C + B[j:]
        
        if j == nB:
            C = C + A[i:]
        
        return C