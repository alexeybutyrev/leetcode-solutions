# Problem: Last Stone Weight
# Language: python3
# Runtime: 36 ms
# Memory: 13.8 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heappush(h, -s)
        while len(h) > 1:
            x = heappop(h)
            y = heappop(h)
            if x != y:
                heappush(h, x-y)
        
        return 0 if not h else -h[0]