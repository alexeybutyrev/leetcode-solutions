# Problem: Sum of K Subarrays With Length at Least M
# Language: python3
# Runtime: 3822 ms
# Memory: 389.1 MB

class Solution:
    def maxSum(self, A: List[int], k: int, M: int) -> int:
        N = len(A)
        
        @cache
        def dp(i,k,ce):
            if N - i - k*M < 0:
                return -inf
            
            if i == N:
                return 0 if k==0 else -inf

            ans = dp(i+1,k,False)
            if ce:
                ans = max(ans, dp(i+1,k,True) + A[i])
            if k > 0:
                if M == 1:
                    return max(ans, A[i] + dp(i+1,k-1, True))
                    
                if M == 2:
                    return max(ans, A[i] + A[i+1] + dp(i+2,k-1, True))
                
            
                return max(ans, A[i] + A[i+1] + A[i+2] + dp(i+3,k-1, True))
            return ans
        
        ans = dp(0,k, False)
        dp.cache_clear()    
        return ans