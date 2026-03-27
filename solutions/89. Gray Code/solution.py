# Problem: Gray Code
# Language: python3
# Runtime: 7 ms
# Memory: 22.9 MB

class Solution:
    def grayCode(self, n: int) -> List[int]:
        A = [0]
        
        for j in range(n):
            A = A + [a + (1 << j) for a in A][::-1]
        
        return A