# Problem: Smallest Pair With Different Frequencies
# Language: python3
# Runtime: 4 ms
# Memory: 19.6 MB

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c = Counter(nums)

        F = {}
        for x,f in c.items():
            if f in F:
                F[f] = min(F[f],x)
            else:
                F[f] = x

        A = list(F.values())
        A.sort()
        if len(A) > 1:
            return A[0], A[1]
        return [-1,-1]