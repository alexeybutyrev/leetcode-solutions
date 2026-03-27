# Problem: Count the Number of Houses at a Certain Distance I
# Language: python3
# Runtime: 427 ms
# Memory: 16.6 MB

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def dra(adj,node,n):
            dist = [inf] * n
            h = []
            heappush(h, (0,node))
            dist[node] = 0
            while h:
                d,u = heappop(h)
                if d > dist[u]: continue
                for v in adj[u]:
                    dv = d + 1
                    if dv < dist[v]:
                        dist[v] = dv
                        heappush(h,(dv, v))

            return dist
        
        graph = defaultdict(set)
        
        for i in range(n):
            if i < n - 1:
                graph[i].add(i+1)
                graph[i+1].add(i)
        x-=1
        y-=1
        graph[x].add(y)
        graph[y].add(x)
        ans = [0] * n
        for node in range(n):
            dist = dra(graph,node,n)
            for x in dist:
                if x:
                    ans[x-1] += 1
        return ans