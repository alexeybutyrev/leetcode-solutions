# Problem: Construct Binary Search Tree from Preorder Traversal
# Language: python3
# Runtime: 24 ms
# Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def walk(node, a):
            #print(a)
            v = node.val
            
            if not a:
                node.left  = None
                node.right = None
                
            ind_left = 0
            for i in range(len(a)):
                if a[i] < v:
                    ind_left = i
                    break
            
            ind_right = 0
            for i in range(len(a)):
                if a[i] > v:
                    ind_right = i
                    break
                    
            if 0 == ind_left:
                node.left = None
            else:
                node.left = TreeNode(a[ind_left])
                if 0 == ind_right:
                    walk(node.left, a[ind_left:])
                else:
                    walk(node.left, a[ind_left:ind_right])
            
            if 0 == ind_right:
                node.right = None
            else:
                node.right = TreeNode(a[ind_right])
                walk(node.right, a[ind_right:])
            
        if not preorder:
            return preorder
        
        root = TreeNode(preorder[0])
        node = root
        walk(node,preorder)
        return root
                