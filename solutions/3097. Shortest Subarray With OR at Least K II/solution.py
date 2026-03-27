# Problem: Shortest Subarray With OR at Least K II
# Language: python3
# Runtime: 1783 ms
# Memory: 35.6 MB

class Solution:
    def minimumSubarrayLength(self, A: List[int], k: int) -> int:
        N = len(A)
        M = 32
        
        
        
        ans = -1
        
        curr = 0    
        c = [0] * M
        def convert(c):
            ans = 0
            for x in range(M):
                if c[x]:
                    ans |= (1<<x)
            return ans
        
        ans = inf
        j = i = 0
        while j < N:
            x = A[j]
            for b in range(M):
                if x & (1<<b):
                    c[b] += 1
            
            curr = convert(c)
            

            while i <= j and curr >= k:
                ans = min(ans, j - i+1) 
                x = A[i]
                for b in range(M):
                    if x & (1<<b):
                        c[b] -= 1
                i += 1
                curr = convert(c)
            
            
            j += 1
        
        return -1 if ans == inf else ans