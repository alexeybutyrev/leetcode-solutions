# Problem: Count Nodes Equal to Average of Subtree
# Language: python3
# Runtime: 819 ms
# Memory: 15.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def count(root):
            n = 0
            s = 0
            def walk(node):
                nonlocal n
                nonlocal s
                if node:
                    n += 1
                    s += node.val
                    walk(node.left)
                    walk(node.right)

            walk(root)
            av = s // n
            
            return +(root.val == av)
        
        ans = 0
        def walk(node):
            nonlocal ans
            if node:
                ans += count(node)
                walk(node.left)
                walk(node.right)
            
        
        walk(root)
        return ans
                