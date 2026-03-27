# Problem: Ugly Number II
# Language: python3
# Runtime: 124 ms
# Memory: 23.8 MB

seen = {1}
for _ in range(30):
    for k in [2,3,5]:
        seen |= {x * k for x in seen}
    
A = sorted(seen)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return A[n-1]
        
