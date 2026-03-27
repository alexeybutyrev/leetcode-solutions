# Problem: Smallest Subtree with all the Deepest Nodes
# Language: python3
# Runtime: 0 ms
# Memory: 19.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        depth = {None: -1}
        
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        max_depth = max(depth.values())
        
        
        def walk(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            L = walk(node.left)
            R = walk(node.right)
            return node if L and R else L or R
        
        return walk(root)