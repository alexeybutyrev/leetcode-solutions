# Problem: Determine the Minimum Sum of a k-avoiding Array
# Language: python3
# Runtime: 56 ms
# Memory: 16.3 MB

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = 0
        A = set()
        for x in range(1,100000):
            if k - x not in A:
                A.add(x)
            if len(A) == n:
                return sum(A)
        