# Problem: Find Minimum Time to Reach Last Room II
# Language: python3
# Runtime: 2194 ms
# Memory: 164.6 MB

class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        h = []

        heappush(h, (0,True,0,0))
        d = defaultdict(lambda: inf)
        d[(0,0)] = 0
        N, M = len(A), len(A[0])
        ans = inf
        D = [(0,1), (1,0), (-1,0), (0,-1)]
        while h:
            t, p, i, j = heappop(h)
            if i == N -1 and j == M - 1:
                return t

            for dx, dy in D:
                x = i + dx
                y = j + dy
                
                if 0 <= x < N and 0 <=  y < M:
                    dt = 1 if p else 2
                    T = max(dt + A[x][y], dt + t)
                    if d[(x,y)] > T:
                        d[(x,y)] = T
                        heappush(h,(T,not p, x,y))
        return d[(N-1,M-1)]