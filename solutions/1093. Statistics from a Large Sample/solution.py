# Problem: Statistics from a Large Sample
# Language: python3
# Runtime: 44 ms
# Memory: 14.5 MB

from bisect import bisect
class Solution:
    def sampleStats(self, A: List[int]) -> List[float]:
        n = sum(A)
        mi   = min([i for i, a in enumerate(A) if a]) * 1.0
        ma   = max([i for i, a in enumerate(A) if a]) * 1.0
        mean = sum([i * a for i, a in enumerate(A) if a]) * 1.0 / n
        
        mode = A.index(max(A)) * 1.0
        
        for i in range(255):
            A[i+1] += A[i]
        ml = bisect(A, (n - 1) / 2)
        mr = bisect(A, (n ) / 2)
        median = (ml + mr) / 2.0
        return [mi, ma, mean, median, mode]