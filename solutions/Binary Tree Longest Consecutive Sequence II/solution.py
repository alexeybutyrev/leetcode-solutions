# Problem: Binary Tree Longest Consecutive Sequence II
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
    def longestConsecutive(self, root: TreeNode) -> int:
        
        def walk(node):
            if node:
                return 1 + walk_down(node) + walk_up(node)
            
            return 0
        
        def walk_down(node):
            if node:
                c1 = None
                if node.left and node.left.val == node.val -1:
                    c1 = 1 + walk_down(node.left)
                
                c2 = None
                if node.right and node.right.val == node.val -1:
                    c2 = 1 + walk_down(node.right)
                
                if c1:
                    if c2:
                        return max(c1, c2)
                    return c1
                if c2: return c2
                return 0
            return 0
        
        def walk_up(node):
            if node:
                c1 = None
                if node.left and node.left.val == node.val+1:
                    c1 = 1 + walk_up(node.left)
                
                c2 = None
                if node.right and node.right.val == node.val+1:
                    c2 = 1 + walk_up(node.right)
                
                if c1:
                    if c2:
                        return max(c1, c2)
                    return c1
                if c2: return c2
                return 0
            return 0
        
        def ans(node):
            if node:
                a = walk(node)
                
                return max(a,ans(node.left),ans(node.right))
            return 0
        return ans(root)