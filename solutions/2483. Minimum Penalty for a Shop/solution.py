# Problem: Minimum Penalty for a Shop
# Language: python3
# Runtime: 141 ms
# Memory: 18.4 MB

class Solution:
    def bestClosingTime(self, C: str) -> int:
        A = [1 if c == "Y" else 0 for c in C]
        
        ans = x = sum(A)
        t = 0
        for i,a in enumerate(A):
            if a == 1:
                x -= 1
            if a == 0:
                x += 1
            if x < ans:
                t = i+1
                ans = x
        return t