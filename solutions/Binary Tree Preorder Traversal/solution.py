# Problem: Binary Tree Preorder Traversal
# Language: python
# Runtime: 16 ms
# Memory: 11.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

            
    def preorderTraversal(self, root, r = []):
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
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        
        return output
            