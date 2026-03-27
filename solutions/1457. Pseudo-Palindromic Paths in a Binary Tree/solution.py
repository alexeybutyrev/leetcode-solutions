# Problem: Pseudo-Palindromic Paths in a Binary Tree
# Language: python3
# Runtime: 4647 ms
# Memory: 111.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def walk(node, c):
            if node:
                c[node.val] += 1
                if not node.left and not node.right:
                    self.ans += sum(v & 1 for v in c.values()) <= 1
                if node.left:
                    walk(node.left, Counter(c))
                
                if node.right:
                    walk(node.right, Counter(c))
        
        walk(root, Counter())
        
        return self.ans
        
                
                
            
            