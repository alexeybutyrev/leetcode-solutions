# Problem: Count Special Integers
# Language: python3
# Runtime: 649 ms
# Memory: 20.5 MB

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        A = [int(x) for x in str(n)]
        N = len(A)
        
        @cache
        def dp(i, flag, lead, mask):
            
            if i == N: return 1    
            
            if flag:
                limit = A[i]
            else:
                limit = 9
            
            ans = 0
            for j in range(limit + 1):
                newFlag = flag and (j == limit)
                newLead = lead and j == 0
                if newLead:
                    ans += dp(i+1, newFlag, newLead, mask)
                else:
                    if mask & (1 << j) == 0:
                        ans += dp(i+1, newFlag, newLead, mask | (1 << j))
            return ans
                    
            
            
        
        return dp(0,True,True,0) - 1
            