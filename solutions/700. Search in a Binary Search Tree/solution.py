# Problem: Search in a Binary Search Tree
# Language: python
# Runtime: 68 ms
# Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or root.val == val:
            return root
        
        return self.searchBST(root.left, val) if val <= root.val else self.searchBST(root.right, val)
    
        