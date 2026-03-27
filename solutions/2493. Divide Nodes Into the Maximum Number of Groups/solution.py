# Problem: Divide Nodes Into the Maximum Number of Groups
# Language: python3
# Runtime: 2364 ms
# Memory: 17.5 MB

class Solution:
    def magnificentSets(self, N: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def max_groups(G):
            def bfs(nodes):
                q = deque()
                seen = set()
                for n in nodes:
                    q.append(n)
                    seen.add(n)
                l = 0
                while q:
                    L = len(q)
                    seen_b = set()
                    for _ in range(L):
                        n = q.popleft()
                        seen_b.add(n)
                        for node in graph[n]:
                            if node in seen_b:
                                return -1
                            if node not in seen:
                                seen.add(node)
                                q.append(node)
                    l += 1

                if len(seen) == N:
                    return l
                return l
            ans = -1
            for node in G:
                ans = max(ans, bfs([node]))
            return ans
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]


        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)

        for u in range(1,N+1):
            union(u,u)
        
        for u, v in edges:
            union(u,v)
        
        groups = defaultdict(list)
        for u in range(1,N+1):
            groups[find(u)].append(u)
        
        
        ans = 0
        for g in groups:
            x = max_groups(groups[g])
            if x == -1:
                return -1
            ans += x
        return ans
            
        
        