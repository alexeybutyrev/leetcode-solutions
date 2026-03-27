# Problem: Delete Leaves With a Given Value
# Language: python3
# Runtime: 134 ms
# Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            
            r = TreeNode(-1)
            r.left = root
            
            parents = {}
            
            def walk(node):
                if node:
                    if node.left:
                        parents[node.left] = (node,'l')
                        walk(node.left)
                    if node.right:
                        parents[node.right] = (node,'r')
                        walk(node.right)
            
            walk(r)
            
            def walk2(node):
                if node:
                    if not node.left and not node.right and node.val == target:
                        p, d = parents[node]
                        if d == "l":
                            p.left = None
                        else:
                            p.right = None
                        walk2(p)
                    else:    
                        walk2(node.left)
                        walk2(node.right)
            
            walk2(r)

            return r.left
                
                        
                        