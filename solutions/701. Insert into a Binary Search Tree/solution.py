# Problem: Insert into a Binary Search Tree
# Language: python3
# Runtime: 132 ms
# Memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        node = root
        
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val,None, None)
                    return root
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val,None, None)
                    return root 
        return TreeNode(val,None, None)
    
                
        
        