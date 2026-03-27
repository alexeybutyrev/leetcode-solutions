# Problem: Russian Doll Envelopes
# Language: python3
# Runtime: 144 ms
# Memory: 16.5 MB

def bs(A, a):
    lo = 0
    hi = len(A) - 1
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        
        if A[mid][0] < a[0] and A[mid][1] < a[1]:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return lo
    
class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        
        A.sort(key = lambda x: (x[0], -x[1]))
        def lic(nums):
            dp = [-10**5]
        
            for n in nums:
                ind = bisect_left(dp,n)

                if ind >= len(dp):
                    dp.append(-1)

                dp[ind] = n

            return len(dp) - 1
        
        return lic([a[1] for a in A])