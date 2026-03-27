# Problem: Minimum Bitwise OR From Grid
# Language: python3
# Runtime: 181 ms
# Memory: 42 MB

class Solution:
    def minimumOR(self, A: List[List[int]]) -> int:
        N = len(A)
        M = len(A[0])
        v = 0
        ans = 0
        for p in range(32,-1,-1):
            v |= (1 << p)
            pr = True
            for x in A:
                for y in x:
                    if  y & v == 0:
                        break
                else:
                    pr = False
                    break
            if not pr:
                ans |= (1<<p)
                v ^= (1<<p)
        return ans