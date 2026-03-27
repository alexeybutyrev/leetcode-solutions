# Problem: Flatten Binary Tree to Linked List
# Language: python3
# Runtime: 40 ms
# Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def conv(node, L, R):
            if not L and not R:
                return node
            
            if L:
                node.right = L 
                node.left = None
                node = node.right
                node = conv(node, L.left, L.right)
                
                
            if R:
                node.right = R 
                node.left = None 
                node = node.right
                node = conv(node, R.left, R.right)
                
            return node
        if root:
            conv(root, root.left, root.right)
    