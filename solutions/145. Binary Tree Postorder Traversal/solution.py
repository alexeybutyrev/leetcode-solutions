# Problem: Binary Tree Postorder Traversal
# Language: python
# Runtime: 20 ms
# Memory: 11.9 MB

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
            
            self._collect(node.right,r)
            r.append(node.val)
        return r
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        stack, output = [root,], []
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
        
        return output[::-1]
        