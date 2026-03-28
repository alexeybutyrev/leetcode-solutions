# Problem: Flip Equivalent Binary Trees
# Language: python3
# Runtime: 28 ms
# Memory: 14.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        def walk(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                
                return walk(node1.left, node2.left) & walk(node1.right, node2.right) | walk(node1.left, node2.right) & walk(node1.right, node2.left)
        
            if not node1 and not node2:
                return True
            return False
    
        return walk(root1, root2)