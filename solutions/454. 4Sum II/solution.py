# Problem: 4Sum II
# Language: python3
# Runtime: 332 ms
# Memory: 34.7 MB

from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        hm = {}
        for i in range(n):
            for j in range(n):
                s = A[i] + B[j]
                if s in hm:
                    hm[s] += 1
                else:
                    hm[s] = 1
        
        count = 0
        for i in range(n):
            for j in range(n):
                s = - (C[i] + D[j])
                if s in hm:
                    count += hm[s]
        return count
        