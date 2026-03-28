# Problem: Construct Binary Search Tree from Preorder Traversal
# Language: python3
# Runtime: 36 ms
# Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(ind_left = 0, ind_right = len(preorder)):
            
            nonlocal pre_idx
            if ind_left == ind_right:
                return None
            
            val = preorder[pre_idx]
            index = ind_hm[val]
            
            pre_idx+=1
            root = TreeNode(val)
            
            root.left  = helper(ind_left, index)
            root.right = helper(index+1, ind_right)
            
            return root
        
        pre_idx = 0
        indorder = sorted(preorder)
        ind_hm = {val:ind for ind,val in enumerate(indorder)}
        
        
        
        return helper()