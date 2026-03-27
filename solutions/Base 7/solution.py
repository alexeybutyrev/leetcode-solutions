# Problem: Base 7
# Language: python3
# Runtime: 28 ms
# Memory: 14.1 MB

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0: return "-" + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)
    