# Problem: Count Artifacts That Can Be Extracted
# Language: python3
# Runtime: 2661 ms
# Memory: 64.4 MB

class Solution:
    def digArtifacts(self, n: int, A: List[List[int]], dig: List[List[int]]) -> int:
        D = set((x,y) for x,y in dig)
        ans = 0
        for (r1,c1,r2,c2) in A:
            BR = False
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    if (r,c) not in D:
                        BR = True
                        break
                if BR:
                    break
            else:
                ans += 1
        return ans
            
            