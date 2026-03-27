# Problem: Maximum Sum of Distinct Subarrays With Length K
# Language: python3
# Runtime: 233 ms
# Memory: 36.1 MB

class Solution:
    def maximumSubarraySum(self, A: List[int], k: int) -> int:
        c = Counter()
        s = 0
        for x in range(k):
            c[A[x]] += 1
            s += A[x]
        
        ans = 0
        if len(c) == k:
            ans = max(ans, s)
        
        for i in range(k,len(A)):
            s -= A[i -k]
            c[A[i-k]] -= 1
            if not c[A[i-k]]: del c[A[i-k]]
            s += A[i]
            c[A[i]] += 1
            if len(c) == k:
                ans = max(ans, s)
        return ans
            
            
            