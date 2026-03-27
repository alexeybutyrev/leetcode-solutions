# Problem: Count Different Palindromic Subsequences
# Language: python3
# Runtime: 804 ms
# Memory: 83.9 MB

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        
        prv = [-1] * N
        nxt = [-1] * N
        
        last = [-1] * 4
        for i in range(N):
            last[A[i]] = i
            prv[i] = tuple(last)
        
        last = [-1] * 4
        for i in range(N-1,-1,-1):
            last[A[i]] = i
            nxt[i] = tuple(last)
        
        @cache
        def dp(i,j):
            ans = 1
            if i <= j:
                
                for x in range(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    
                    if i0 >= 0 and i <= i0 <= j:
                        ans +=1
                    
                    if i0 >= 0 and i0 < j0:
                        ans += dp(i0+1,j0-1)
                        
            ans %= MOD
            return ans
        return dp(0,N-1) - 1