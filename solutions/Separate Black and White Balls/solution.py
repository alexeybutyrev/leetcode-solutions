# Problem: Separate Black and White Balls
# Language: python3
# Runtime: 101 ms
# Memory: 18.4 MB

class Solution:
    def minimumSteps(self, s: str) -> int:
        L = list(s)
        n = 0
        ans = 0
        while L:
            if L.pop() == '1':
                ans += n
            else:
                n += 1
        return ans