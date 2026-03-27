# Problem: Smallest Number With All Set Bits
# Language: python3
# Runtime: 0 ms
# Memory: 17.5 MB

class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(bin(n).replace("0","1")[2:],2)