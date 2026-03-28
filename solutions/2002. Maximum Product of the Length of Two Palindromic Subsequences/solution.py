# Problem: Maximum Product of the Length of Two Palindromic Subsequences
# Language: python3
# Runtime: 2840 ms
# Memory: 21.6 MB

class Solution:
    def maxProduct(self, S: str) -> int:
        N = len(S)
        is_pali = lambda x: x == x[::-1]
        
        M = {}
        @cache
        def dp(mask,i,s):
            if is_pali(s):
                M[mask] = len(s)
            
            if i < N:
                for j in range(i,N):
                    if mask & (1 << j) == 0:
                        dp(mask | (1<<j), j+1, s + S[j])
        
        dp(0,0,'')
        A = [(v,k) for k,v in M.items()]
        A.sort(reverse = True)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i][1] & A[j][1] == 0:
                    ans = max(ans,A[i][0] * A[j][0])
        return ans
                
        