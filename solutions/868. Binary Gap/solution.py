# Problem: Binary Gap
# Language: python3
# Runtime: 4 ms
# Memory: 19.7 MB

class Solution:
    def binaryGap(self, n: int) -> int:
        A = [ (x, len(list(y)) ) for x,y in groupby(bin(n)[2:]) ]
        if A[-1][0] == '0':
            A.pop()

        if len(A) == 1:
            return 1 if A[0][1] > 1 else 0
        ans = 0
        for x,y in A:
            if x == '0':
                ans = max(ans, y + 1)

        return ans