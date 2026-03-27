# Problem: Merge Two Binary Trees
# Language: python3
# Runtime: 82 ms
# Memory: 17.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def walk(t1,t2):
            if not t1 and not t2:
                return None
            if not t1: return t2
            if not t2: return t1
            ans = TreeNode(t1.val + t2.val)
            ans.left = walk(t1.left,t2.left)
            ans.right = walk(t1.right, t2.right)
            return ans
        return walk(root1,root2)