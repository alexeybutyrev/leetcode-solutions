# Problem: Split Array Largest Sum
# Language: python3
# Runtime: 69 ms
# Memory: 13.9 MB

class Solution:
    def splitArray(self, A: List[int], m: int) -> int:
        
        def valid(x):
            ns = 0
            curr = 0
            for a in A:
                if curr + a > x:
                    curr = a
                    ns += 1
                else:
                    curr += a
                
            return ns + 1
        
        lo = max(A)
        hi = sum(A)

        while lo <= hi:
            mid = (lo + hi) // 2
            
            if valid(mid) <= m:
                hi = mid - 1
                ans = mid
            else:
                lo = mid + 1
               
                
        
        return ans