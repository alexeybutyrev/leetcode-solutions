# Problem: Binary Tree Pruning
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def prune(node):
            if node:
                l = prune(node.left)
                r = prune(node.right)
                if 0 == l:
                    node.left = None
                if 0 == r:
                    node.right = None
                return l + node.val + r
            else:
                return 0
        
        prune(root)
        if root and not root.left and not root.right and 0 == root.val:
            return None
        return root