# Problem: Count Good Nodes in Binary Tree
# Language: python3
# Runtime: 232 ms
# Memory: 33.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def walk(node, val):
            nonlocal count
            if node:
                if node.val >= val:
                    val = node.val
                    count += 1
                walk(node.left,val)
                walk(node.right,val)
        
        walk(root,-inf)
        
        return count