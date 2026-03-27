# Problem: Increasing Order Search Tree
# Language: python3
# Runtime: 38 ms
# Memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans = t = TreeNode()
        def walk(node):
            nonlocal t
            if node:
                walk(node.left)
                t.right = TreeNode(node.val)
                t = t.right
                walk(node.right)
        
        walk(root)
        return ans.right