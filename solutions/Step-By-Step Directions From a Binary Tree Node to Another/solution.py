# Problem: Step-By-Step Directions From a Binary Tree Node to Another
# Language: python3
# Runtime: 819 ms
# Memory: 77.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # create graph
        graph = defaultdict(dict)
        
        def walk(node, parent):
            if node:
                if node.left:
                    graph[node.val]['L'] = node.left.val
                    graph[node.left.val]['U'] = node.val
                    walk(node.left, node)
                
                if node.right:
                    graph[node.val]['R'] = node.right.val
                    graph[node.right.val]['U'] = node.val
                    walk(node.right, node)
        
        if root.left:
            graph[root.val]['L'] = root.left.val
            graph[root.left.val]['U'] = root.val
            walk(root.left, root)

        if root.right:
            graph[root.val]['R'] = root.right.val
            graph[root.right.val]['U'] = root.val
            walk(root.right, root)
        
        
        q = deque([(startValue,"")])
        seen = {startValue}
        while q:
            L = len(q)
            for _ in range(L):
                node, p = q.popleft()
                if node == destValue:
                    return p
                for d in graph[node]:
                    if graph[node][d] not in seen:
                        seen.add(graph[node][d])
                        q.append((graph[node][d],p+d))
        
        return ""