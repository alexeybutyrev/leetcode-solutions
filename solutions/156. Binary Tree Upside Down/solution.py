# Problem: Binary Tree Upside Down
# Language: python3
# Runtime: 60 ms
# Memory: 16.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        ans = root
        while ans.left:
            ans = ans.left
        
        def walk(node,l,r):
            if node.left:
                walk(node.left,node.left.left, node.left.right)
            
            if node.right:
                walk(node.right,node.right.left, node.right.right)
            node.left = None
            node.right = None
            if l:
                l.left = r      
                l.right = node 
        
        walk(root, root.left, root.right)
        return ans
                