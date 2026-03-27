# Problem: Maximum Depth of Binary Tree
# Language: python
# Runtime: 28 ms
# Memory: 14.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _md(self, node, depth):
        if not node:
            return depth
        
        return max(self._md(node.left, depth+1), self._md(node.right, depth+1))
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._md(root, 0)