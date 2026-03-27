# Problem: The Most Similar Path in a Graph
# Language: python3
# Runtime: 2599 ms
# Memory: 27 MB

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        graph = defaultdict(set)
        for x,y in roads:
            graph[x].add(y)
            graph[y].add(x)
        
        
        M = len(targetPath)
        @cache
        def dp(node,j):
            if j == M:
                return (0,[])
            x = 0 if names[node] == targetPath[j] else 1
            
            d = inf
            seq = []
            for nb in graph[node]:
                
                d1, s1 = dp(nb,j+1)
                
                if d1 < d:
                    d = d1
                    seq = [node] + s1
            
            return d + x,seq
        
        d = inf
        ans = []
        for i in range(n):
            d1,p = dp(i,0)
            if d > d1:
                d = d1
                ans = p
            
        
        return ans
    
