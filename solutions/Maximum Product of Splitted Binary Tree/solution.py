# Problem: Maximum Product of Splitted Binary Tree
# Language: python3
# Runtime: 315 ms
# Memory: 144.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        
        graph = defaultdict(list)
        edges = list()
        def walk(node):
            if node:
                if node.left:
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    walk(node.left)
                    edges.append((node, node.left))
                if node.right:
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    walk(node.right)
                    edges.append((node, node.right))
        walk(root)
        @cache
        def sm(l,r):
            ans = l.val
            for node in graph[l]:
                if node != r:
                    ans += sm(node,l)
            return ans
        s = 0
        for l,r in edges:
            s = max(sm(l,r) * sm(r,l),s)
        
        return s % MOD
                    
        
        