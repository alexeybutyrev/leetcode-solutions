# Problem: Maximum Non Negative Product in a Matrix
# Language: python3
# Runtime: 143 ms
# Memory: 24.5 MB

class Solution:
    def maxProductPath(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        MOD = 10**9 + 7
        q = deque([(0,0,A[0][0])])
        ans = -1
        seen = {(0,0,A[0][0])}
        while q:
            i,j,p =  q.popleft()
            if i == N - 1 and j == M - 1:
                if p >= 0:
                    ans = max(ans, p) 
            for dx,dy in [(1,0),(0,1)]:
                x = i + dx
                y = j + dy
                if x < N and y < M and (x,y,p * A[x][y]) not in seen:
                    seen.add((x,y,p * A[x][y]))
                    q.append((x,y,p * A[x][y]))

        return -1 if ans < 0 else ans % MOD