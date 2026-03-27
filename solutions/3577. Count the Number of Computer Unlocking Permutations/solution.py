# Problem: Count the Number of Computer Unlocking Permutations
# Language: python3
# Runtime: 20 ms
# Memory: 31.9 MB

class Solution:
    def countPermutations(self, A: List[int]) -> int:
        N = len(A)
        MOD = 10**9 + 7

        if min(A) != A[0] or min(A) in A[1:]: return 0
        
        ans = 1
        for x in range(1, N):
            ans *= x
            ans %= MOD
        return ans