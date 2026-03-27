# Problem: Majority Frequency Characters
# Language: python3
# Runtime: 11 ms
# Memory: 18 MB

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        c2 = Counter(c.values())
        print(c)
        print(c2)
        mx = max(c2.values())
        
        res = -1
        for x in c2:
            if c2[x] == mx and res < x:
                res = x

        ans = ""
        for x in c:
            if c[x] == res:
                ans += x
        return ans