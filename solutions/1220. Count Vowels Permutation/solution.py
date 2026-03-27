# Problem: Count Vowels Permutation
# Language: python3
# Runtime: 473 ms
# Memory: 173.8 MB

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        V = ['a', 'e', 'i', 'o', 'u']
        MOD = 10**9 + 7
        @cache
        def dp(i,l):
            if i == n: return 1
            if l == 'a':
                return dp(i+1,'e')
            elif l == 'e':
                return (dp(i+1,'a') + dp(i+1,'i')) % MOD
            elif l == 'i':
                return (dp(i+1,'a') + dp(i+1,'e') + dp(i+1,'o') + dp(i+1,'u')) % MOD
            elif l == 'o':
                return (dp(i+1,'i') + dp(i+1,'u')) % MOD
            else:
                return dp(i+1,'a')
        n-=1
        ans = 0
        for x in V:
            ans += dp(0,x)
            ans %= MOD
        return ans