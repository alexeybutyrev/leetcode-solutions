# Problem: Find the Minimum Possible Sum of a Beautiful Array
# Language: python3
# Runtime: 119 ms
# Memory: 26.1 MB

class Solution:
    def minimumPossibleSum(self, n: int, t: int) -> int:
        s = 0
        ans = 0
        curr = 1
        seen = set()
        while s < n:
            if t - curr not in seen:
                seen.add(curr)
                ans += curr
                s += 1
                curr += 1
                
            else:
                curr += 1
        return ans