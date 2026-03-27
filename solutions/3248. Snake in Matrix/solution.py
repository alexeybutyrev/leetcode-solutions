# Problem: Snake in Matrix
# Language: python3
# Runtime: 65 ms
# Memory: 16.5 MB

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for c in commands:
            if c == "RIGHT":
                ans += 1
            elif c == "LEFT":
                ans -= 1
            elif c == "DOWN":
                ans += n
            else:
                ans -= n
        return ans