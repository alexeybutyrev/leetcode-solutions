# Problem: Find the Winning Player in Coin Game
# Language: python3
# Runtime: 35 ms
# Memory: 16.5 MB

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        a = True
        while True:
            if x < 1 or y < 4:
                return "Bob" if a else "Alice"
            else:
                x -= 1
                y -= 4
                a = not a
        return "Bob" if a else "Alice"