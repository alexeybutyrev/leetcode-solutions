# Problem: Construct String from Binary Tree
# Language: python3
# Runtime: 52 ms
# Memory: 16.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    return str(node.val)
                if not node.right:
                    return str(node.val) + "(" + dfs(node.left) +")"
                return str(node.val) + "(" + dfs(node.left) + ")(" + dfs(node.right) +")"
            else:
                return ""
        
        if not root:
            return ""
        
        return dfs(root)