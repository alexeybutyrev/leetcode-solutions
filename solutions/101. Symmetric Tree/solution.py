# Problem: Symmetric Tree
# Language: python
# Runtime: 24 ms
# Memory: 12.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _is_sym(self, left_nodes, right_nodes):
        if not left_nodes and not right_nodes:
            return True
        
        ln, rn = [],[]
        for i in range(len(left_nodes)):
            # check values
            if left_nodes[i].val != right_nodes[i].val:
                return False
            
            if left_nodes[i].left or right_nodes[i].right:
                if left_nodes[i].left and right_nodes[i].right:
                        ln.append(left_nodes[i].left)
                        rn.append(right_nodes[i].right)
                else:
                    return False
            
            if left_nodes[i].right or right_nodes[i].left:
                if left_nodes[i].right and right_nodes[i].left:
                        ln.append(left_nodes[i].right)
                        rn.append(right_nodes[i].left)
                else:
                    return False
        return self._is_sym(ln,rn)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if root.left and root.right:
            return self._is_sym([root.left], [root.right])
        else:
            return False
        