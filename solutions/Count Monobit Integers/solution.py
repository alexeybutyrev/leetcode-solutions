# Problem: Count Monobit Integers
# Language: python3
# Runtime: 39 ms
# Memory: 19.5 MB

class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        for i in range(1, n+1):
            if "0" not in bin(i)[2:]:
                ans += 1
        return ans