# Problem: Minimum Length of String After Operations
# Language: python3
# Runtime: 142 ms
# Memory: 19 MB

class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0

        for k,x in c.items():
            
            if x %2 == 0:
                ans += 2
            else:
                ans += 1
        return ans