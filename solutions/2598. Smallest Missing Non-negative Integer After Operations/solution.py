# Problem: Smallest Missing Non-negative Integer After Operations
# Language: python3
# Runtime: 1180 ms
# Memory: 33.3 MB

class Solution:
    def findSmallestInteger(self, A: List[int], v: int) -> int:
        c = Counter()
        
        for x in A:
            c[x % v] += 1
        N = len(A)
        for i in range(N):
            if c[i%v] == 0:
                return i
            c[i%v] -=1
        
        return N