# Problem: Find Minimum Time to Reach Last Room I
# Language: python3
# Runtime: 135 ms
# Memory: 17.2 MB

class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        h = []

        heappush(h, (0,0,0))
        d = defaultdict(lambda: inf)
        d[(0,0)] = 0
        N, M = len(A), len(A[0])
        ans = inf
        D = [(0,1), (1,0), (-1,0), (0,-1)]
        while h:
            t, i, j = heappop(h)
            if i == N -1 and j == M - 1:
                return t

            for dx, dy in D:
                x = i + dx
                y = j + dy
                
                if 0 <= x < N and 0 <=  y < M:
                    T = max(1 + A[x][y], 1 + t)
                    if d[(x,y)] > T:
                        d[(x,y)] = T
                        heappush(h,(T,x,y))
        return d[(N-1,M-1)]
                    
            
            