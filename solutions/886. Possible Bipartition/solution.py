# Problem: Possible Bipartition
# Language: python3
# Runtime: 809 ms
# Memory: 20.2 MB

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for u in range(1,n+1):
            union(u,u)
        
        for node in graph:
            p = find(node)
            p2 = find(graph[node][0])
            for n2 in graph[node][1:]:
                union(n2,p2)
                if find(p) == find(p2):
                    return False
        
        
        return True
    