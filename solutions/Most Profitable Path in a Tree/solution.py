# Problem: Most Profitable Path in a Tree
# Language: python3
# Runtime: 223 ms
# Memory: 75 MB

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        N = len(amount)
        time = [0] * N
        P = {}
        
        def dfs(node, parent, l):
            time[node] = l
            P[node] = parent
            for nb in graph[node]:
                if nb != parent:
                    dfs(nb, node, l + 1)
        dfs(0,-1,0)
        
        btime = [inf] * N 
        curr = bob
        t = 0
        ans = 0
        while curr != 0:
            btime[curr] = t
            if btime[curr] < time[curr]:
                amount[curr] = 0
            elif btime[curr] == time[curr]:
                amount[curr] //= 2
            curr = P[curr]
            t += 1
        self.ans = -inf
        
        def dfs2(node, parent, s):
            d = 0
            for nb in graph[node]:
                if nb != parent:
                    dfs2(nb, node, s + amount[nb])
                    d += 1
            if d == 0:
                self.ans = max(self.ans, s)
        
        dfs2(0,-1,amount[0])
        return self.ans
            