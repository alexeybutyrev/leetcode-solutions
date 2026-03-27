# Problem: Sum of Subarray Minimums
# Language: python3
# Runtime: 342 ms
# Memory: 21.6 MB

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        N = len(A)
        stack = [N]
        ans = 0
        l = 0
        MOD = 10**9 + 7
        
        for i in range(N-1,-1,-1):
            while stack[-1] < N and A[stack[-1]] > A[i]:
                ind = stack.pop()
                l -= A[ind] * (stack[-1] - ind)
                l += A[i] * (stack[-1] - ind)
            l += A[i]
            stack.append(i)
            ans += l
            ans %= MOD
        return ans % MOD