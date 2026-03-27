# Problem: Maximum Average Subtree
# Language: python3
# Runtime: 63 ms
# Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.ans = 0
        def walk(node):
            if node:
                lv,lc = walk(node.left)
                rv,rc = walk(node.right)
                self.ans = max(self.ans, (node.val + lv+rv)/(1 + lc+rc))
                return (node.val + lv+rv),(1 + lc+rc)
            else:
                return 0,0
        
        _,_ = walk(root)
        return self.ans