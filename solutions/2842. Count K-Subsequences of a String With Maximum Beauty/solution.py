# Problem: Count K-Subsequences of a String With Maximum Beauty
# Language: python3
# Runtime: 82 ms
# Memory: 18.6 MB

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        count = Counter(s)
        if len(count) < k:
            return 0
        bar = sorted(count.values())[-k]
        res = 1
        mod = 10 ** 9 + 7
        m = 0
        for v in count.values():
            if v > bar:
                k -= 1
                res = res * v % mod
            if v == bar:
                m += 1
        return res * comb(m, k) * pow(bar, k, mod) % mod
        
        
        return dp(0,0)
        
            