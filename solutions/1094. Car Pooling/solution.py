# Problem: Car Pooling
# Language: python3
# Runtime: 56 ms
# Memory: 15 MB

class Solution:
    def carPooling(self, A: List[List[int]], C: int) -> bool:
        A.sort(key = lambda x: x[1])
        h = []
        for p,x,y in A:
            while h and h[0][0] <= x:
                x1,y1,p1 = heappop(h)
                C += p1
            if p <= C:
                heappush(h, (y,x,p))
                C -= p
            else:
                return False
        return True
                
                