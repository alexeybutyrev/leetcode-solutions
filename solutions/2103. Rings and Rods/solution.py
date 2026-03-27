# Problem: Rings and Rods
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def countPoints(self, A: str) -> int:
        r = [0] * 10
        
        for i in range(len(A) // 2):
            col = 'RGB'.index(A[2*i])
            r[int(A[2*i + 1])] |= 1 << col
        return sum(c == 0b111 for c in r)