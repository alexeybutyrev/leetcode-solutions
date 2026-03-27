# Problem: Remove Zeros in Decimal Representation
# Language: python3
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n)
        s = s.replace("0","")
        return int(s)