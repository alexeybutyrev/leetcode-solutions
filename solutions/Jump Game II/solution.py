# Problem: Jump Game II
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def jump(self, A: List[int]) -> int:
        
        
        count = 0 
        N = len(A)

        futhest = 0
        next_jump = 0
        for i in range(N - 1):
            futhest = max(futhest, i + A[i])
            if i == next_jump:
                count += 1
                next_jump = futhest
        
        return count
            