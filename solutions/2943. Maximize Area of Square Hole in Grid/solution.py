# Problem: Maximize Area of Square Hole in Grid
# Language: python3
# Runtime: 3 ms
# Memory: 19.6 MB

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        YC = set(vBars)
        
        
        def findlen(A):
            if not A: return 1
            
            A.sort()
            C = [A[0]]
            ans = 2
            for x in A[1:]:
                
                if x == C[-1] + 1:
                    C.append(x)
                    ans = max(ans, len(C) + 1)
                else:
                    C = [x]
            return ans
        
        mx = findlen(hBars)
        my = findlen(vBars)
        c = min(mx,my)
        return c * c