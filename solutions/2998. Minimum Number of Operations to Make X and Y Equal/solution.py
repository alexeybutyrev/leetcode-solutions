# Problem: Minimum Number of Operations to Make X and Y Equal
# Language: python3
# Runtime: 99 ms
# Memory: 20.5 MB

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        h = [(0,x)]
        if x == y: return 0
        count = 0
        seen = {x}
        ans = inf
        while h:
            c,x = heappop(h)
            if c > ans: continue
            if x == y:
                ans = c
            
            if x % 11 == 0 and x // 11 not in seen:
                seen.add(x//11)
                heappush(h,(c + 1, x//11))
                
            if x % 5 == 0 and x // 5 not in seen:
                seen.add(x//5)
                heappush(h,(c + 1, x//5))
            if x + 1 not in seen:
                seen.add(x+1)
                heappush(h,(c + 1, x+1))
            if x - 1 not in seen:
                seen.add(x-1)
                heappush(h,(c + 1, x-1))
            
        
        return ans