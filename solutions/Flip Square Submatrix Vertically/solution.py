# Problem: Flip Square Submatrix Vertically
# Language: python3
# Runtime: 0 ms
# Memory: 19.7 MB

class Solution:
    def reverseSubmatrix(self, A: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        ANS = []
        A = [list(x) for x in zip(*A)]
        x,y = y,x
        for i,r in enumerate(A):
            if x <= i < x + k:
                nr = r[:y] + r[y:y+k][::-1] + r[y+k:]
                ANS.append(nr)
            else:
                ANS.append(r)
        ANS = [list(x) for x in zip(*ANS)]
        return ANS
            