# Problem: Minimum Capacity Box
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def minimumIndex(self, capacity: list[int], S: int) -> int:
        ans = -1
        c = inf
        for i,x in enumerate(capacity):
            if x >= S and x < c:
                ans = i
                c = x
        return ans