# Problem: Maximum Sum of Almost Unique Subarray
# Language: python3
# Runtime: 456 ms
# Memory: 20 MB

class Solution:
    def maxSum(self, A: List[int], m: int, k: int) -> int:
        c = Counter(A[:k])
        curr = sum(A[:k])
        
        if len(c) >= m: 
            ans = curr
        else:
            ans = 0
            
        for i in range(k,len(A)):
            curr -= A[i-k]
            curr += A[i]
            c[A[i-k]] -= 1
            c[A[i]] += 1
            if not c[A[i-k]]:
                del c[A[i-k]]
            if len(c) >= m:
                ans = max(ans, curr)
        
        return ans
    