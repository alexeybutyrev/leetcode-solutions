# Problem: Maximum Subarray Min-Product
# Language: python3
# Runtime: 1248 ms
# Memory: 25.6 MB

class Solution:
    def maxSumMinProduct(self, A: List[int]) -> int:
        N = len(A)
        S = [0]
        ans = 0
        for a in A:
            S.append(S[-1]+a)
        stack = [0]
        for i,a in enumerate(A):
            while stack[-1]>0 and A[stack[-1]-1]>=a:
                ch = A[stack.pop()-1]
                cw = S[i] - S[stack[-1]]
                ans = max(ans, ch*cw)
            stack.append(i+1)
        
        while stack[-1]>0:
            ch = A[stack.pop()-1]
            cw = S[len(A)] - S[stack[-1]]
            ans = max(ans, ch*cw)
        MOD = 10**9 + 7
        return ans % MOD

        