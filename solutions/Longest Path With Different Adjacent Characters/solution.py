# Problem: Longest Path With Different Adjacent Characters
# Language: python3
# Runtime: 2779 ms
# Memory: 195.7 MB

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        edges = []
        graph = defaultdict(list)
        for i,a in enumerate(parent):
            if a != -1 and s[a] != s[i]:
                graph[a].append(i)
                graph[i].append(a)

        @cache        
        def dfs(node, parent):
            ans = 0
            for v in graph[node]:
                if v != parent:
                    ans = max(ans, 1 + dfs(v,node))
            return ans
        ans = 1
        for u in graph:
            for v in graph[u]:
                ans = max(ans, 2 + dfs(u,v))
        return ans
            
        
        