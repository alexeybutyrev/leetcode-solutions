# Problem: Prime Number of Set Bits in Binary Representation
# Language: python3
# Runtime: 168 ms
# Memory: 14.4 MB

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum ( (665772 >> bin(i).count('1')) & 1 for i in range(left, right + 1))