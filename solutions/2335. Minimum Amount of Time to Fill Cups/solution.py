# Problem: Minimum Amount of Time to Fill Cups
# Language: python3
# Runtime: 42 ms
# Memory: 13.7 MB

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        h = []
        for a in amount:
            if a != 0:
                heappush(h,-a)
        count = 0
        while len(h) > 1:
            count += 1
            #print(h)
            x1 = heappop(h)
            x2 = heappop(h)
            
            if x1 + 1 != 0:
                heappush(h, x1 + 1)
            
            if x2 + 1 != 0:
                heappush(h, x2 + 1)
        if h:
            return count - h[0]
        return count

            