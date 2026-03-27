# Problem: Minimum Number of Chairs in a Waiting Room
# Language: python3
# Runtime: 45 ms
# Memory: 16.7 MB

class Solution:
    def minimumChairs(self, s: str) -> int:
        x = ans = 0
        for c in s:
            if c == 'E':
                x += 1
            else:
                x -=1
            ans = max(ans, x)
        return ans
                