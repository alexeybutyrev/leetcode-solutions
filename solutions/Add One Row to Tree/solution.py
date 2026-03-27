# Problem: Add One Row to Tree
# Language: python3
# Runtime: 48 ms
# Memory: 16.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            r = TreeNode(v)
            r.left = root
            return r
        
        q = deque([root])
        while d > 2 and q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            d -= 1
        
        for node in q:
            l = node.left
            r = node.right
            node.left  = TreeNode(v)
            node.left.left = l
            node.right = TreeNode(v)
            node.right.right = r
        
        return root    