# Problem: Maximum Good People Based on Statements
# Language: python3
# Runtime: 2133 ms
# Memory: 14.4 MB

class Solution:
    def maximumGood(self, A: List[List[int]]) -> int:
        N = len(A)
        
        ans = 0
        for p in range(1<<N, 1<<(N+1)):
            for i in range(N):
                if p & (1 <<i) == 0: continue
                flag = True
                for j in range(N):
                    if A[i][j] == 2: continue
                    if (A[i][j] == 1 and p & (1 << j) == 0) or (A[i][j] == 0 and p & (1 << j) != 0):
                        flag = False
                        break
                if not flag:
                    break
            else:
                ans = max(ans, bin(p)[3:].count('1'))
        
        return ans
                                