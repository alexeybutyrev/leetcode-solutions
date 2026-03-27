# Problem: All Elements in Two Binary Search Trees
# Language: python3
# Runtime: 348 ms
# Memory: 22.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def walk(node, A):
            if node:
                walk(node.left,A)
                A.append(node.val)
                walk(node.right,A)
        
        A = []
        B = []
        walk(root1, A)
        walk(root2, B)
        
        C = []
        N1,N2 = len(A), len(B)
        i = j = 0
        
        while i < N1 and j < N2:
            if A[i] <= B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j += 1
        
        if i < N1:
            return C + A[i:]
        else:
            return C + B[j:]