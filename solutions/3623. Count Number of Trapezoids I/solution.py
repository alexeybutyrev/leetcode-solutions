# Problem: Count Number of Trapezoids I
# Language: python3
# Runtime: 175 ms
# Memory: 63.6 MB

class Solution:
    def countTrapezoids(self, A: List[List[int]]) -> int:
        MOD = 10**9 + 7
        P = Counter()

        for x,y in A:
            P[y] += 1
        
        s = 0
        for y in P:
            
            P[y] = P[y] * (P[y] - 1) // 2

            s += P[y]
        ans = 0
        for y in P:
            ans += (s-P[y]) * P[y]
            ans %= MOD
            s -= P[y]
        return ans