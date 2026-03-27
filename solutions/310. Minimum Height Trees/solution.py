# Problem: Minimum Height Trees
# Language: python3
# Runtime: 421 ms
# Memory: 28.7 MB

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def dfs(n,p):
            ans = 0
            for nb in graph[n]:
                if nb != p:
                    ans = max(ans, 1 + dfs(nb,n))
            return ans
        
        
        
        c = [inf] * n
        for node in range(n):
            a = 0
            for nb in graph[node]:
                a = max(a, 1 + dfs(nb,node))
            c[node] = min(c[node], a)
        
        min_path = min(c)
        ans = []
        for k,v in enumerate(c):
            if v == min_path:
                ans.append(k)
        return ans