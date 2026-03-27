# Problem: Sum of Digits in the Minimum Number
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        d = min(A)
        
        s = 0 
        for l in str(d):
            s += int(l)
        
        return 1 if s % 2 == 0 else 0