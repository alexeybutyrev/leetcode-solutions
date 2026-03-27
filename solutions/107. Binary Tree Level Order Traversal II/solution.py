# Problem: Binary Tree Level Order Traversal II
# Language: python3
# Runtime: 32 ms
# Memory: 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        q = [root]
        
        res = []
        while q:
            l = len(q)
            layer = []
            for _ in range(l):                
                v = q.pop(0)
                layer.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            res.append(layer)
        
        return list(reversed(res))