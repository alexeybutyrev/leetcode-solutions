# Problem: Number of Beautiful Integers in the Range
# Language: python3
# Runtime: 120 ms
# Memory: 17.4 MB

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        k = k
        s = ""

        @lru_cache(None)
        def dfs(idx, tight, cnt, rem, lz):
            nonlocal s, k
            if idx == len(s):
                return cnt == 0 and rem == 0 and not lz

            res = 0
            up = int(s[idx]) if tight else 9
            for digit in range(up+1):
                newcnt = cnt
                newlz = lz and digit == 0
                if digit % 2:
                    newcnt += 1
                elif not newlz:
                    newcnt -= 1
                newrem = (rem*10 + digit) % k
                res += dfs(idx+1, tight and (digit == up), newcnt, newrem, newlz)
            return res






        s = str(high)
        res = dfs(0, 1, 0, 0, True)

        s = str(low-1)
        dfs.cache_clear()
        res -= dfs(0, 1, 0, 0, True)

        return res