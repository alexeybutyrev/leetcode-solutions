# Problem: N-ary Tree Level Order Traversal
# Language: python3
# Runtime: 126 ms
# Memory: 16.1 MB

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def _lod(self, node, l = 0, res = []):
        if node:
            while len(res) <= l:
                res.append([])
                
            res[l].append(node.val)
        for c in node.children:
            self._lod(c, l +1, res)
        
        return res

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return root
        
        return self._lod(root, 0, [[]])
    