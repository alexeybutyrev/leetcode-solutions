# Problem: Binary Tree Inorder Traversal
# Language: python
# Runtime: 20 ms
# Memory: 11.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _collect(self, node, r = []):
        if node:
            self._collect(node.left,r)
            r.append(node.val)
            self._collect(node.right,r)
        return r
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, output = [], []
        while (root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        
        return output
    