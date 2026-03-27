# Problem: Sum Multiples
# Language: python3
# Runtime: 73 ms
# Memory: 13.9 MB

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for x in range(1,n+1):
            if (x % 3 ==0 ) or (x %5 ==0) or (x%7 ==0):
                ans += x
        return ans
            