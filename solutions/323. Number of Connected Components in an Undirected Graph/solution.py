# Problem: Number of Connected Components in an Undirected Graph
# Language: python3
# Runtime: 116 ms
# Memory: 17.4 MB

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u):
            if u not in seen:
                seen.add(u)
                for v in graph[u]:
                    dfs(v)
        
        seen =set()
        ans = 0
        for u in range(n):
            if u not in seen:
                ans += 1
                dfs(u)
        return ans