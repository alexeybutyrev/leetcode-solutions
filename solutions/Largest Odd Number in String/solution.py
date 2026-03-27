# Problem: Largest Odd Number in String
# Language: python3
# Runtime: 58 ms
# Memory: 17.9 MB

class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        N = len(num)
        for i in range(N-1,-1,-1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ans