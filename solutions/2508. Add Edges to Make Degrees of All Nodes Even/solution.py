# Problem: Add Edges to Make Degrees of All Nodes Even
# Language: python3
# Runtime: 2164 ms
# Memory: 74.2 MB

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        c = Counter()
        G = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            c[u] ^= 1
            c[v] ^= 1
            G.add((u,v))
            G.add((v,u))
        
        s = set()
        for u in range(1,n+1):
            if c[u]:
                s.add(u)
        
        f = lambda u,v: (u,v) not in G
        
        if len(s) == 0:
            return True
        if len(s) == 2:
            u,v = s
            for w in range(1,n+1):
                if f(u,w) and f(v,w): 
                    return True
        
        if len(s) == 4:
            u,v,p,q = s
            return f(u,v) and f(p,q) or \
               f(u,p) and f(v,q) or \
               f(u,q) and f(v,p)
            
        return False
            
                    
        