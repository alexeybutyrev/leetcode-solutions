# Problem: Difference Between Maximum and Minimum Price Sum
# Language: python3
# Runtime: 2733 ms
# Memory: 213.4 MB

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @cache
        def dfs(node, par):
            ans = price[node]
            for nb in graph[node]:
                if nb != par:
                    ans = max(ans, price[node] + dfs(nb,node))
            return ans
        
        ans = 0
        for u in range(n):
            ans = max(ans, dfs(u,-1) - price[u])
        
        return ans
    