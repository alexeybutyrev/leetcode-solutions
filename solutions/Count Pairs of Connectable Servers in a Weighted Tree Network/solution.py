# Problem: Count Pairs of Connectable Servers in a Weighted Tree Network
# Language: python3
# Runtime: 2622 ms
# Memory: 18.9 MB

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], SS: int) -> List[int]:
        graph = defaultdict(list)
        N = len(edges) + 1
        c = Counter()
        for a,b,w in edges:
            graph[a].append(b)
            graph[b].append(a)
            c[(a,b)] = c[(b,a)] = w
            c[(a,a)] = 0
            c[(b,b)] = 0
        
        
        def dfs(u,v,d):
            ans = int(d % SS == 0)
            for w in graph[v]:
                if w != u:
                    ans += dfs(v, w, d +  c[(w,v)])
            return ans
        
        
        ANS = [] 
        for u in range(N):
            res = count = 0
            nodes = []
            for v in graph[u]:
                c1 = dfs(u,v,c[(u,v)])
                nodes.append(c1)
                count += c1
            for x in nodes:
                res += x * (count - x)
            ANS.append(res//2)
        
        
        return ANS
        
        
            
            