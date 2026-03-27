# Problem: Cousins in Binary Tree
# Language: python3
# Runtime: 28 ms
# Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def search(node, l, parent, x):
            if node:
                if node.val == x:
                    return (l,parent)
                
                l1 = search(node.left,  l+1, node.val,  x)
                l2 = search(node.right, l+1, node.val,  x)
                
                if l1:
                    return l1
                
                if l2:
                    return l2
            else:
                return None
        
        (lx, px) = search(root, 0, 0, x)
        (ly, py) = search(root, 0, 0, y)
        

        return lx == ly and px != py
            