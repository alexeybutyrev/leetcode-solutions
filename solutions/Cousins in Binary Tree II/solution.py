# Problem: Cousins in Binary Tree II
# Language: python3
# Runtime: 1927 ms
# Memory: 191.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = Counter()
        parent = {}
        def walk(node, p):
            
            if node:
                if p:
                    parent[node] = p
                else:
                    parent[node] = -1
                
                sm = 0
                if node.left:
                    sm += node.left.val
                    walk(node.left,node)
                    
                if node.right:
                    sm += node.right.val
                    walk(node.right,node)
                
                s[node] = sm
        
        walk(root, None)
        mapping = Counter()
        
        q = deque([root])
        ans = []
        while q:
            L = len(q)
            Nodes = []
            sm = 0
            for _ in range(L):
                node = q.popleft()
                sm += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                Nodes.append(node)
            
            for n in Nodes:
                mapping[n] = sm - s[parent[n]]
        
        def walk2(node):
            if node:
                node.val = mapping[node]
                walk2(node.left)
                walk2(node.right)
        mapping[root] = 0
        walk2(root)
        return root