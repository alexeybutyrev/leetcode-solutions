# Problem: Sum of GCD of Formed Pairs
# Language: python3
# Runtime: 235 ms
# Memory: 36.8 MB

class Solution:
    def gcdSum(self, A: list[int]) -> int:
        P = [A[0]]
        M = [A[0]]
        for x in A[1:]:
            y = max(M[-1],x)
            M.append(y)
            g = gcd(y,x)

            P.append(g)
            

        P.sort()

        P = deque(P)
        ans = 0
        while len(P) > 1:
            a,b = P.popleft(), P.pop()
            ans += gcd(a,b)
        return ans
        