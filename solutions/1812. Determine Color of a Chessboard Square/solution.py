# Problem: Determine Color of a Chessboard Square
# Language: python3
# Runtime: 48 ms
# Memory: 14.1 MB

class Solution:
    def squareIsWhite(self, C: str) -> bool:
        a = ord(C[0]) - ord('a')
        b = int(C[1])
        return (a + b) % 2 == 0