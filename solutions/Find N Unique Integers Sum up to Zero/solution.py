# Problem: Find N Unique Integers Sum up to Zero
# Language: python3
# Runtime: 0 ms
# Memory: 17.7 MB

class Solution:
    def sumZero(self, n: int) -> List[int]:
        A = []
        for x in range(1,n):
            A.append(x)
        A.append(-sum(A))
        return A