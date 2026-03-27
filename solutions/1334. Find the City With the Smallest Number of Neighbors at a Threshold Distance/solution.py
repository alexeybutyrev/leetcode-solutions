# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Language: python3
# Runtime: 459 ms
# Memory: 17.6 MB

class Solution:
    def findTheCity(self, n, edges, maxd):
        
        D = [ [inf]*n for _ in range(n)]

        for u,v,c in edges:
            D[u][v] = D[v][u] = c

        for u in range(n):
            D[u][u] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        r = {sum(x <= maxd for x in D[i]): i for i in range(n)}
        return r[min(r)]
            