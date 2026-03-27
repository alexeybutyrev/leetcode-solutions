# Problem: Take Gifts From the Richest Pile
# Language: python3
# Runtime: 49 ms
# Memory: 14 MB

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = []
        for x in gifts:
            heappush(h,-x)
        ans = 0
        for _ in range(k):
            x = heappop(h)
            x = -x
            left = floor(sqrt(x))
            if left:
                heappush(h,-left)
            if not h:
                return 0
        return -sum(h)