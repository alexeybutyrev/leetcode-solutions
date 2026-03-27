# Problem: Number of Nodes in the Sub-Tree With the Same Label
# Language: python3
# Runtime: 3027 ms
# Memory: 180.7 MB

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        A = [0] * n
        def dfs(node, par):
            c = Counter()
            for nb in graph[node]:
                if nb != par:
                    c += dfs(nb, node)
            c[labels[node]] += 1
            A[node] = c[labels[node]]
            return c
        
        dfs(0,-1)
        return A
        
       