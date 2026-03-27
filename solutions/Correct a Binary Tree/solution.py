# Problem: Correct a Binary Tree
# Language: python3
# Runtime: 153 ms
# Memory: 31.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        p = {}
        def walk(node):
            if node:
                if node.left:
                    p[node.left] = node
                    walk(node.left)
                if node.right:
                    p[node.right] = node
                    walk(node.right)
        walk(root)
        
        q = deque([root])
        while q:
            L = len(q)
            seen = set()
            for _ in range(L):
                node = q.popleft()
                for n in [node.left, node.right]:
                    if n:
                        q.append(n)
                        seen.add(n)
            for n in q:
                if n.right in seen:
                    par = p[n]
                    if par.left == n:
                        par.left = None
                    else:
                        par.right = None
                    return root
        return root