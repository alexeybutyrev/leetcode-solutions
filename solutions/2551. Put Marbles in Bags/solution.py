# Problem: Put Marbles in Bags
# Language: python3
# Runtime: 1029 ms
# Memory: 30.4 MB

class Solution:
    def putMarbles(self, A: List[int], k: int) -> int:
        h1 = []
        h2 = []
        
        for i in range(len(A)-1):
            heappush(h1, A[i] + A[i+1])
            heappush(h2, -(A[i] + A[i+1]))
        
        s1 = 0
        s2 = 0
        for _ in range(k-1):
            s1 += heappop(h1)
            s2 += heappop(h2)
        return -(s2+s1)