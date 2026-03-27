# Problem: Number Complement
# Language: python3
# Runtime: 20 ms
# Memory: 14.2 MB

class Solution:
    def findComplement(self, num: int) -> int:
        
        return (1 << num.bit_length()) - 1 - num
                