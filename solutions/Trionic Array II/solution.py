# Problem: Trionic Array II
# Language: python3
# Runtime: 211 ms
# Memory: 32 MB

class Solution:
    def maxSumTrionic(self, A: List[int]) -> int:
        N = len(A)
        if N < 3: return 0 # Or whatever your base case is
        
        # 1. Standard Prefix Sums
        F = [0] * (N + 1)
        for i in range(N):
            F[i+1] = F[i] + A[i]
            
        ans = -float('inf')
        i = 0
        
        while i < N - 1:
            # --- Part 1: First Increase ---
            start = i
            min_prefix = F[i]
            while i < N - 1 and A[i] < A[i+1]:
                min_prefix = min(min_prefix, F[i])
                i += 1
            
            p = i # First Peak
            if p == start: # Didn't increase
                i += 1
                continue
                
            # --- Part 2: Decrease ---
            while i < N - 1 and A[i] > A[i+1]:
                i += 1
            
            q = i # Valley
            if q == p: # Didn't decrease
                # Don't increment i here; we might be at the start of a new climb
                continue
                
            # --- Part 3: Second Increase ---
            # We check if we can climb again from the valley 'q'
            while i < N - 1 and A[i] < A[i+1]:
                i += 1
                # Calculate sum from the best start point in Part 1 to current end
                ans = max(ans, F[i+1] - min_prefix)
            
            # Optimization: The end of the second increase is the start 
            # of a potential new 'peak' for the next sequence.
            # We reset i to the valley 'q' to catch overlapping patterns.
            i = q 
            
        return ans if ans != -float('inf') else 0