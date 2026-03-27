# Problem: Maximum Difference Between Even and Odd Frequency I
# Language: python3
# Runtime: 7 ms
# Memory: 17.8 MB

class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        min1 = min2 = inf
        max1 = max2 = 0
        E,O = [],[]
        for k,v in c.items():
            if v % 2 == 0:
                E.append(v)
                max1 = max(max1,v)
                min1 = min(min1,v)
            else:
                O.append(v)
        ans = -inf
        for i in range(len(O)):
            for j in range(len(E)):
                ans = max(ans, O[i] - E[j])
        return ans