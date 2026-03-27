# Problem: Vertical Order Traversal of a Binary Tree
# Language: python3
# Runtime: 28 ms
# Memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from heapq import *
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        q = []
        heappush(q,(root.val, 0,root))
        res = defaultdict(list)
        while q:
            l = len(q)
            new_heap = []
            for _ in range(l):
                value, v, node = heappop(q)           
                res[v].append(value)
                
                if node.left:
                    heappush(new_heap,(node.left.val, v-1,node.left))
                if node.right:
                    heappush(new_heap,(node.right.val, v+1,node.right))
            q = new_heap

        
        result = []
        for key in sorted(res.keys()):
            result.append(res[key])
        
        
        return result
                    
                