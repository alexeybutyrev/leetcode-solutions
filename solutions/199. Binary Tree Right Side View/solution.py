# Problem: Binary Tree Right Side View
# Language: python
# Runtime: 16 ms
# Memory: 12.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return root
        q, res, sol = [root], [], []
        
        level = 0
        
        while q:
            res.append([])
            n_nodes = len(q)
            for i in range(n_nodes):
                node = q.pop(0)
                res[level].append(node.val)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
            sol.append(res[level][-1])
            level += 1
        
        return sol
        