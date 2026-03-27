# Problem: Shortest Cycle in a Graph
# Language: python3
# Runtime: 4064 ms
# Memory: 14.5 MB

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(i):
            
            d = defaultdict(lambda: inf)
            q = deque([i])
            d[i] = 0
            ans = inf
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if d[v] == inf:
                        d[v] = d[u] + 1
                        q.append(v)
                    elif v!=i and d[u] <= d[v]:
                        ans = min(ans,d[u] + d[v] + 1)
            return ans
        
        ans = min(bfs(i) for i in range(n))
        return -1 if ans == inf else ans