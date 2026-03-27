# Problem: Boundary of Binary Tree
# Language: python3
# Runtime: 49 ms
# Memory: 18.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = [root.val]
        def walk(node):
            if not node or not node.left and not node.right: return
            
            ans.append(node.val)
            if node.left:
                walk(node.left)
            else:
                walk(node.right)
        walk(root.left)

        def walk(node):
            if node:
                walk(node.left)
                if node != root and not node.left and not node.right:
                    ans.append(node.val)
                walk(node.right)
        walk(root)

        # right
        def walk(node):
            if not node or not node.left and not node.right: return                
            if node.right:
                walk(node.right)
            else:
                walk(node.left)
            ans.append(node.val)
        
        walk(root.right)
        
        return ans
                    
                