# Problem: Binary Tree Cameras
# Language: python3
# Runtime: 44 ms
# Memory: 14.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        
        covered = {None}
        def dfs(node, par = None):
            nonlocal ans
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered) or node.left not in covered or node.right not in covered:

                    ans += 1
                    covered.add(node.left)
                    covered.add(node.right)
                    covered.add(par)
                    covered.add(node)
        
        dfs(root)
        return ans