# Problem: Two Sum Less Than K
# Language: python3
# Runtime: 43 ms
# Memory: 16.3 MB

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        A.sort()
        
        i, j  = 0, len(A) - 1
        max_s = -1
        while i < j:
            s = A[i] + A[j]
            if s < K:
                i+=1
                max_s = max(max_s, s)
            else:
                j -= 1
                
        return max_s