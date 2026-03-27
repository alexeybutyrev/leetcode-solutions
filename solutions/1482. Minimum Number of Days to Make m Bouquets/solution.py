# Problem: Minimum Number of Days to Make m Bouquets
# Language: python3
# Runtime: 2262 ms
# Memory: 27.4 MB

class Solution:
    def minDays(self, A: List[int], m: int, k: int) -> int:
        N = len(A)

            
        def check(x):
            hm = Counter()
            ans = 0
            flow = 0
            for a in A:
                flow = 0 if a > x else flow + 1
                if flow >= k:
                    flow = 0
                    ans += 1
                    if ans == m: 
                        return True
            
            return False
            
        lo = 0
        hi = 1_000_000_000
        
        while lo < hi:
            mid = lo + hi >> 1
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
                
                
        return lo if check(lo) else -1 
        