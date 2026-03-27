# Problem: Count Number of Pairs With Absolute Difference K
# Language: python3
# Runtime: 149 ms
# Memory: 14.3 MB

class Solution:
    def countKDifference(self, A: List[int], k: int) -> int:
        c = Counter()
        ans = 0
        for x in A:
            ans += c[x-k]
            ans += c[x+k]
            c[x] += 1
        return ans