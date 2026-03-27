# Problem: Find Center of Star Graph
# Language: python3
# Runtime: 711 ms
# Memory: 52.2 MB

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans=0
        d = 0
        c = Counter()
        for u,v in edges:
            c[u]+=1
            c[v]+=1
        
        for x in c:
            if c[x] > d:
                d = c[x]
                ans = x
        return ans