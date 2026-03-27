# Problem: Minimum Operations to Write the Letter Y on a Grid
# Language: python3
# Runtime: 569 ms
# Memory: 16.7 MB

class Solution:
    def minimumOperationsToWriteY(self, A: List[List[int]]) -> int:
        N = len(A)
        
        def iny(i,j):
            if i == j and j < N // 2: return True
            if i >= N // 2 and j == N // 2: return True
            
            if i < N // 2 and j == N - i-1 : return True
            return False
        
        def check(x,y):
            ans = 0
            for i in range(N):
                for j in range(N):
                    if iny(i,j):
                        if A[i][j] != x:
                            ans += 1
                    else:
                        if A[i][j] != y:
                            ans += 1
            return ans
        
        ans = inf
        for x,y in product([0,1,2], [0,1,2]):
            if x != y:
                ans = min(ans, check(x,y))
        
        return ans