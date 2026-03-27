# Problem: Maximum Number of Removable Characters
# Language: python3
# Runtime: 4615 ms
# Memory: 30.1 MB

class Solution:
    def maximumRemovals(self, s: str, p: str, A: List[int]) -> int:
        def is_sub(s,t):
            t = iter(t)
            return all( c in t for c in s)
        
        def possible(k):
            ns = ""
            S = set(A[:k+1])
            
            for i,l in enumerate(s):
                if i in S:
                    continue
                else:
                    ns += l

            return is_sub(p,ns)
        
        lo = 0
        hi = len(A)
        while lo < hi:
            mid = lo + hi >> 1
            if possible(mid):
                lo = mid + 1
            else:
                hi = mid
                
                
        
        return min(lo+1,len(A)) if possible(lo) else lo