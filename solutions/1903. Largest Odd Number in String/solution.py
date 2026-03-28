# Problem: Largest Odd Number in String
# Language: python3
# Runtime: 84 ms
# Memory: 15.4 MB

class Solution:
    def largestOddNumber(self, num: str) -> str:
        N = len(num)
        ans = ""
        for j in range(N-1,-1,-1):
            if int(num[j]) % 2 != 0:
                return num[0:j+1]
        return ans