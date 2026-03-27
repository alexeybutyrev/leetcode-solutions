# Problem: Minimum Cost to Convert String II
# Language: python3
# Runtime: 1877 ms
# Memory: 51.6 MB

class Solution:
    def minimumCost(self, S: str, T: str, O: List[str], U: List[str], C: List[int]) -> int:
        # intialize and create cost matrix C['a']['b'] = min possibe or inf

        CM = defaultdict(lambda : defaultdict(lambda: inf))
        for x in O:
            CM[x][x] = 0
        for x in U:
            CM[x][x] = 0
        graph = defaultdict(set)

        seen = set()
        q = []
        for u,v,c in zip(O,U,C):
            graph[u].add(v)
            CM[u][v] = min(CM[u][v], c)
            if (u,v) not in seen:
                seen.add((u,v))
                q.append((u,v))
        
        
        # find min distances
        for u,v in q:
            for w in graph[v]:
                if CM[u][w] > CM[u][v] + CM[v][w]:
                    CM[u][w] = CM[u][v] + CM[v][w]
                    q.append((u,w))
        
        VKEYS = defaultdict(set)
        UKEYS = CM.keys()
        for u in CM:
            VKEYS[u] = set(v for v in CM[u])
        
            
        jumps = defaultdict(list)
        for i,x in enumerate(S):
            for u in UKEYS:
                if S[i:].startswith(u):
                    for v in VKEYS[u]:
                        if T[i:].startswith(v):
                            jumps[i].append((i + len(v),CM[u][v]))
        N = len(S)
        @cache
        def dp(i):
            if i == N: return 0
            ans = inf
            if S[i] == T[i]:
                ans = min(ans, dp(i+1))
            for j,c in jumps[i]:
                ans = min(ans, c + dp(j))
            return ans
        ans = dp(0)
        return -1 if ans == inf else ans
