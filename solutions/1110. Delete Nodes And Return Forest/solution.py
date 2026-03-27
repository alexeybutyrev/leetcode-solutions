# Problem: Delete Nodes And Return Forest
# Language: python3
# Runtime: 58 ms
# Memory: 17 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.ans = []        
        def walk(node,d):
            if node:
                check = False
                if node.left: 
                    if node.left.val in to_delete:
                        t = node.left
                        node.left = None
                        walk(t,True)
                
                if node.right:
                    if node.right.val in to_delete:
                        t = node.right
                        node.right = None
                        walk(t,True)
                
                if d:
                    if node.val not in to_delete:
                        self.ans.append(node)
                        walk(node.left,False)
                        walk(node.right,False)
                    else:
                        walk(node.left,True)
                        walk(node.right,True)
                else:
                    walk(node.left,False)
                    walk(node.right,False)
        
        walk(root, True)
        return self.ans
                
                    