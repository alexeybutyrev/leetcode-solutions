# Problem: Minimum Cost to Convert String I
# Language: python3
# Runtime: 423 ms
# Memory: 21.2 MB

from string import ascii_lowercase
class Solution:
    def minimumCost(self, S: str, T: str, O: List[str], U: List[str], C: List[int]) -> int:
        
        # intialize and create cost matrix C['a']['b'] = min possibe or inf

        CM = defaultdict(lambda : defaultdict(lambda: inf))
        for x in ascii_lowercase:
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
        
        

        for u,v in q:
            for w in graph[v]:
                if CM[u][w] > CM[u][v] + CM[v][w]:
                    CM[u][w] = CM[u][v] + CM[v][w]
                    q.append((u,w))
        
        ans = 0
        for s,t in zip(S,T):
            
            ans += CM[s][t]
        
        return -1 if inf == ans else ans
        
        