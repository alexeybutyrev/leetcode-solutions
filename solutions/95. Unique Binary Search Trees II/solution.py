# Problem: Unique Binary Search Trees II
# Language: python3
# Runtime: 43 ms
# Memory: 18.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import product
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:        
        def create_bts(A = list(range(1,n+1))):
            if not A:
                return [None]
            trees = []
            for i in range(len(A)):
                L = create_bts(A[:i])
                R = create_bts(A[i+1:])
                for (l,r) in product(L,R):
                    node = TreeNode(A[i])
                    node.left = l
                    node.right = r
                    trees.append(node)
            return trees
        
        return create_bts()