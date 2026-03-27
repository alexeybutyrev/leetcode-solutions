# Problem: Maximum Total Importance of Roads
# Language: python3
# Runtime: 1353 ms
# Memory: 45.1 MB

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        c = Counter()
        for x in  range(n):
            c[x]+=1
        for u,v in roads:
            c[u]+=1
            c[v]+=1
        A = [(v,k) for k,v in c.items()]
        A.sort()
        W = [0]*n
        for i,(_,k) in enumerate(A):
            W[k]=i+1
        ans = 0
        for u,v in roads:
            ans+= W[u]+W[v]
        return ans