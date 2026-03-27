# Problem: Apply Operations on Array to Maximize Sum of Squares
# Language: python3
# Runtime: 4099 ms
# Memory: 30.6 MB

class Solution:
    def maxSum(self, A: List[int], k: int) -> int:
        c = Counter()
        for a in A:
            for i in range(35):
                if ((1 << i) & a):
                    c[i] += 1
        
        MOD = 10**9 + 7
        ans = 0
        for _ in range(k):
            curr = 0
            for i in range(35):
                if c[i]:
                    c[i] -= 1
                    curr += (1 << i)
                    curr %= MOD
            ans += curr * curr % MOD
            ans %= MOD
        return ans