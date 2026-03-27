# Problem: Number of Subsequences That Satisfy the Given Sum Condition
# Language: python3
# Runtime: 844 ms
# Memory: 28.5 MB

class Solution:
    def numSubseq(self, A: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        A.sort()
        N = len(A)
        j = N-1
        i = 0
        ans = 0
        while i <= j:
            if A[j] + A[i] <= target:
                ans += pow(2,j-i, MOD)
                ans %= MOD
                i += 1
            else:
                j -= 1
        return ans