# Problem: Count Commas in Range
# Language: python3
# Runtime: 971 ms
# Memory: 19.4 MB

class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        for x in range(1000,n+1):
            ans += int(floor(log(x,1000)))
        return ans