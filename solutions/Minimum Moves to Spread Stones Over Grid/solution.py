# Problem: Minimum Moves to Spread Stones Over Grid
# Language: python3
# Runtime: 2064 ms
# Memory: 19.6 MB

class Solution:
    def minimumMoves(self, A: List[List[int]]) -> int:
        N = 3
        
        @cache
        def check(A):
            for i in range(N):
                for j in range(N):
                    if A[i][j] != 1:
                        return False
            return True
        
        def make_tuple(A):
            S = []
            for a in A:
                S.append(tuple(a))
            return tuple(S)
        
        S = make_tuple(A)
        seen = set(S)
        q = deque()
        q.append(S)
        count = 0
        while q:
            L = len(q)
            for _ in range(L):
                A = q.popleft()
                if check(A): return count
                
                B = [list(a) for a in A]
                
                for i in range(N):
                    for j in range(N):
                        if B[i][j] > 1:
                            for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                                x = i + dx
                                y = j + dy
                                if 0 <= x < N and 0 <= y < N and (x,y) != (i,j):
                                    B[i][j] -= 1
                                    B[x][y] += 1
                                    S = make_tuple(B)
                                    if S not in seen:
                                        seen.add(S)
                                        q.append(S)
                                    B[i][j] += 1
                                    B[x][y] -= 1
                
            count += 1
            
        return count
        