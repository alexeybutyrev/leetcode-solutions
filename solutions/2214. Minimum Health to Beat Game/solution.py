# Problem: Minimum Health to Beat Game
# Language: python3
# Runtime: 601 ms
# Memory: 28.4 MB

class Solution:
    def minimumHealth(self, A: List[int], armor: int) -> int:
        ans = sum(A) + 1
        x = 0
        for a in A:
            if a <= armor and a > x:
                x = a
            if a>= armor:
                x = armor
        return ans - x
            