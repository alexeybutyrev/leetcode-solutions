# Problem: Find the Score Difference in a Game
# Language: python3
# Runtime: 7 ms
# Memory: 19.3 MB

class Solution:
    def scoreDifference(self, A: List[int]) -> int:
        f = 0
        s = 0
        fa = True
        for i,x in enumerate(A):
            if x & 1:
                fa = not fa
            if (i + 1) % 6 == 0:
                fa = not fa
            if fa:
                f += x
            else:
                s += x
                

        return f - s