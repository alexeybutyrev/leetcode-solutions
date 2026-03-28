# Problem: Construct Target Array With Multiple Sums
# Language: python3
# Runtime: 320 ms
# Memory: 20 MB

class Solution:
    def isPossible(self, A: List[int]) -> bool:
        
        N = len(A)
        if sum(A) == N:
            return True
        if N == 1:
            return A[0] ==1
        h = []
        s = 0
        for a in A:
            heappush(h,-a)
            s += a
        
        c = 0
        while h[0] < -1:
            print(h)
            v = -heappop(h)
            rest = s - v
            if rest == 1:
                return True
            x = v % rest
            if x == 0 or x == v:
                return False
            heappush(h,-x)
            s = s - v + x
            
        return sum(h) == -N
        