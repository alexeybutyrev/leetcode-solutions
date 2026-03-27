# Problem: Max Points on a Line
# Language: python3
# Runtime: 906 ms
# Memory: 32.2 MB

class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        if N == 1: return 1

        def check(i,j,k):
            x1,y1 = A[i]
            x2,y2 = A[j]
            x3,y3 = A[k]

            x21 = x2 - x1
            y21 = y2 - y1

            x31 = x3 - x1
            y31 = y3 - y1

            return x31*y21 == x21 * y31
        
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)


        for i in range(N):
            for j in range(i+1,N):
                union((i,j),(i,j))
                for k in range(j+1,N):
                    if check(i,j,k):
                        union((i,j),(i,k))
        ans = 1

        d = Counter()
        for i in range(N):
            for j in range(i+1,N):
                d[find((i,j))] += 1
        
        return max(d.values())+1