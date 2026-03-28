# Problem: Most Stones Removed with Same Row or Column
# Language: python3
# Runtime: 1664 ms
# Memory: 15 MB

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        q = deque()
        
        count = 0
        
        seen = set()
        for i,(x,y) in enumerate(stones):
            if i not in seen:
                visited = set([i])
                xset = set([x])
                yset = set([y])

                while True:
                    N = len(visited)
                    for i,(xn,yn) in enumerate(stones):
                        if i not in visited and (xn in xset or yn in yset):
                            xset.add(xn)
                            yset.add(yn)
                            visited.add(i)
                    if len(visited) == N:
                        break
                if len(visited) > 1:
                    count += len(visited) - 1
            seen |= visited
        
        return count