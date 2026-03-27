# Problem: Smallest Range Covering Elements from K Lists
# Language: python3
# Runtime: 180 ms
# Memory: 23.1 MB

class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:
        h = []
        N = len(A)
        mx = -inf
        for i in range(N):
            heappush(h, (A[i][0], i, 0))
            mx = max(mx, A[i][0])
        s,e = 0, inf
        while len(h) == N:
            mn, r, c = heappop(h)
            
            if mx - mn < e-s:
                s = mn
                e = mx
            
            if c < len(A[r])-1:
                heappush(h, (A[r][c+1], r, c + 1))
                mx = max(mx, A[r][c+1])
        
        return [s,e]