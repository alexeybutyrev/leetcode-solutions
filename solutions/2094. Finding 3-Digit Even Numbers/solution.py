# Problem: Finding 3-Digit Even Numbers
# Language: python3
# Runtime: 5393 ms
# Memory: 14.4 MB

class Solution:
    def findEvenNumbers(self, A: List[int]) -> List[int]:
        N = len(A)
        s = set()
        for i in range(N):
            if A[i]:
                for j in range(N):
                    if j != i:
                        for k in range(N):
                            if k != i  and k != j and A[k] % 2 == 0:
                                s.add(100 * A[i] + 10 * A[j] + A[k])
        
        return sorted(s)
                    