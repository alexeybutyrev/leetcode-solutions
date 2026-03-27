# Problem: Course Schedule IV
# Language: python3
# Runtime: 2575 ms
# Memory: 17.6 MB

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        D = [[False] * n for _ in range(n)]
        
        seen = set()
        for u,v in prerequisites:
            D[u][v] = True
            seen.add(v)
        
        for u in range(n):
            if u not in seen:
                D[u][u] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    D[i][j] |= (D[i][k] and D[k][j])
        
        ans = []
        for u,v in queries:
            ans.append(D[u][v])
        return ans