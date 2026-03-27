# Problem: All Ancestors of a Node in a Directed Acyclic Graph
# Language: python3
# Runtime: 1161 ms
# Memory: 111.9 MB

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        rgraph = defaultdict(list)
        c = Counter()
        for u,v in edges:
            rgraph[v].append(u)
            graph[u].append(v)
            c[u] += 1
        
        ans = [set() for _ in range(n)]
        
        @cache
        def walk(u,r):
            for v in graph[u]:
                ans[v].add(r)
                walk(v,r)
        @cache
        def dfs(u):
            walk(u,u)
            for v in rgraph[u]:
                dfs(v)
                
        
        for x in range(n):
            if not c[x]:
                dfs(x)
        
        
        return [sorted(x) for x in ans]
            