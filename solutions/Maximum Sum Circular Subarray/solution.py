# Problem: Maximum Sum Circular Subarray
# Language: python3
# Runtime: 688 ms
# Memory: 18.9 MB

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        def kadane(A):
            
            curr = ans = A[0]
            for a in A[1:]:
                curr = max(curr + a, a)
                ans = max(ans,curr)
            return ans
        if len(A) == 1:
            return A[0]
        return max(kadane(A), sum(A) + kadane( [-a for a in A[1:] ]))
        
        
    