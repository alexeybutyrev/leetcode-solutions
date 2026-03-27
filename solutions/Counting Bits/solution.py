# Problem: Counting Bits
# Language: python3
# Runtime: 80 ms
# Memory: 23.7 MB

A = []
for i in range(10**5+1):
    A.append(bin(i)[1:].count("1"))
class Solution:
    def countBits(self, n: int) -> List[int]:
        return A[0:n+1]
        