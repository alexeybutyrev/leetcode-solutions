# Problem: Largest 3-Same-Digit Number in String
# Language: python3
# Runtime: 37 ms
# Memory: 16.3 MB

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for k,v in groupby(num):
            if len(list(v)) >= 3:
                ans = max(ans, k)
        return ans * 3 