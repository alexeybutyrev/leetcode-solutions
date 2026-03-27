# Problem: Count Pairs of Points With Distance k
# Language: python3
# Runtime: 2383 ms
# Memory: 30.8 MB

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        c = Counter()
        ans = 0
        for x,y in coordinates:
            for j in range(k+1):
                ans += c[(x ^ j, y ^ (k-j))]
            c[(x, y)] += 1
        return ans