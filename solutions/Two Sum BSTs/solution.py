# Problem: Two Sum BSTs
# Language: python3
# Runtime: 87 ms
# Memory: 23.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        s = set()
        def walk(node):
            if node:
                s.add(node.val)
                walk(node.left)
                walk(node.right)
        
        walk(root1)
        
        def walk(node):
            if node:
                if target - node.val in s:
                    return True
                return walk(node.left) or walk(node.right)
            return False
        
        return walk(root2)