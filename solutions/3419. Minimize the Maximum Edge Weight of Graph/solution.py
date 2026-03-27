# Problem: Minimize the Maximum Edge Weight of Graph
# Language: python3
# Runtime: 822 ms
# Memory: 76.4 MB

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], T: int) -> int:
        graph = defaultdict(set)
        
        W = defaultdict(lambda: inf)
        for v,u,w in edges:
            W[(u,v)] = min(W[(u,v)], w)
            graph[u].add(v)


        D = [ inf] * n
        D[0] = 0
        q = deque([(0,0)])
        while q:
            L = len(q)
            for _ in range(L):
                u,m = q.popleft()
                for v in graph[u]:
                    mx = max(m, W[(u,v)])
                    if D[v] > mx:
                        D[v] = mx
                        q.append((v,mx))
                    

        ans = max(D)
        return -1 if ans == inf else ans
            