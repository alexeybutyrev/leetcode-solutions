# Problem: Sum of Number and Its Reverse
# Language: python3
# Runtime: 5046 ms
# Memory: 13.8 MB

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        for i in range(num+1):
            r = int(str(i)[::-1])
            if i + r == num:
                return True
        return False