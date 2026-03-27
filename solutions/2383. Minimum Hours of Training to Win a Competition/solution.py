# Problem: Minimum Hours of Training to Win a Competition
# Language: python3
# Runtime: 48 ms
# Memory: 13.8 MB

class Solution:
    def minNumberOfHours(self, N: int, X: int, A: List[int], B: List[int]) -> int:
        ans = 0
        for x in B:
            if X > x:
                X += x
            else:
                ans += x - X + 1
                X = x + 1 + x
        
        

        return ans + max(0, sum(A) + 1 - N)
        
                    
            