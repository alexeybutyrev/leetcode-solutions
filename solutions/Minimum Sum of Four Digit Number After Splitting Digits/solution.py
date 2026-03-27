# Problem: Minimum Sum of Four Digit Number After Splitting Digits
# Language: python3
# Runtime: 28 ms
# Memory: 13.9 MB

class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        ans = inf
        for p in permutations([0,1,2,3]):
            ans = min(ans, int(s[p[0]] + s[p[1]]) + int(s[p[2]] + s[p[3]]))
            ans = min(ans, int(s[p[0]]) + int(s[p[1]] + s[p[2]] + s[p[3]]))
            ans = min(ans, int(s[p[0]]+s[p[1]] +s[p[2]]) + int(s[p[3]]))
        return ans
        