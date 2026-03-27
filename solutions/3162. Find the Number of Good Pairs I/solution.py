# Problem: Find the Number of Good Pairs I
# Language: python3
# Runtime: 56 ms
# Memory: 16.7 MB

class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], k: int) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] % (B[j] * k) == 0:
                    ans += 1
        return ans