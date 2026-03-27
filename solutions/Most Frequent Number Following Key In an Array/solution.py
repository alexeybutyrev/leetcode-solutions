# Problem: Most Frequent Number Following Key In an Array
# Language: python3
# Runtime: 88 ms
# Memory: 14.2 MB

class Solution:
    def mostFrequent(self, A: List[int], key: int) -> int:
        N = len(A)
        c = Counter()
        for i in range(1,N):
            if A[i-1] == key:
                c[A[i]] += 1
        return max((v,k) for k,v in c.items())[1]
                