# Problem: The Time When the Network Becomes Idle
# Language: python3
# Runtime: 3977 ms
# Memory: 68.9 MB

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        N = len(patience)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dist = Counter()
        
        seen = {0}
        q = deque([0])
        d = 0
        while q:
            L = len(q)
            d += 1
            for _ in range(L):
                node = q.popleft()
                for v in graph[node]:
                    if v not in seen:
                        dist[v] = d
                        q.append(v)
                        seen.add(v)
        

        ans = 0
        for i in range(1,N):
            d = dist[i]
            p = patience[i]
            ls = 2*d - 1
            lrt = (ls // p) * p
            t = lrt + 2 * d
            ans = max(ans, t)
        
        return ans + 1