# Problem: Find Leaves of Binary Tree
# Language: python3
# Runtime: 32 ms
# Memory: 14.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def prun(node):
            if node:
                if node.left:
                    if node.left.left is None and node.left.right is None:
                        ans.append(node.left.val)
                        node.left = None
                    else:
                        prun(node.left)
                
                if node.right:
                    if node.right.left is None and node.right.right is None:
                        ans.append(node.right.val)
                        node.right = None
                    else:
                        prun(node.right)
        
        A = []
        while root:    
            if not root.left and not root.right:
                A.append([root.val])
                return A
            ans = []
            prun(root)
            A.append(ans)
        return A
                        