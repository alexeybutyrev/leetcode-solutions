# Problem: Matrix Similarity After Cyclic Shifts
# Language: python3
# Runtime: 3 ms
# Memory: 19.5 MB

class Solution:
    def areSimilar(self, A: List[List[int]], k: int) -> bool:
        N,M = len(A), len(A[0])
        k %=M
        B = []
        for i,a in enumerate(A):
            b = []
            if i & 1 == 0:
                b = a[k:] + a[:k]
            else:
                b =  a[k:] + a[:k]
            B.append(b)
            
        return A == B