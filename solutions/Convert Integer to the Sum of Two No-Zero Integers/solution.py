# Problem: Convert Integer to the Sum of Two No-Zero Integers
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1,n):
            if '0' not in str(x) and '0' not in str(n-x):
                return [x,n-x]
        