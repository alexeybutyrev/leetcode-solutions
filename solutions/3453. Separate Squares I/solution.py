# Problem: Separate Squares I
# Language: python3
# Runtime: 1902 ms
# Memory: 48.4 MB

class Solution:
    def separateSquares(self, A: List[List[int]]) -> float:
        
        

        def f(B):
            L = 0
            R = 0
            for x,y,l in A:
                if B > y:
                    if B >= y + l:
                        L += l * l
                    else:
                        d1 = min(B-y, y + l)
                        d2 =  max(0, l - d1)
                        L += d1 * l
                        R += d2 * l
                else:
                    R += l * l
                
                
                
            return L < R

        lo = min(y for x,y,l in A)
        hi = max(y+l for x,y,l in A)
        EPS = 1e-5

        mid_before = inf
        
        while lo < hi:
            mid = (lo + hi) * 0.5 
            mid_after = mid
            if abs(mid_after - mid_before) < EPS:
                return mid
            if not f(mid):
                hi = mid
            else:
                lo = mid
            mid_before = mid
            
        return mid
            