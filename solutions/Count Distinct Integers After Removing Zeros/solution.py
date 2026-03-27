# Problem: Count Distinct Integers After Removing Zeros
# Language: python3
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def countDistinct(self, n: int) -> int:
        L = len(str(n))
        S = str(n)
        P = [1]
        for i in range(1,L+1):
            P.append(P[-1] * 9)
        
        ans = 0
        for i in range(1,L):
            ans += P[i]
        
        for i in range(L):
            d = int(S[i])
            if d == 0:
                return ans
            ans += (d - 1) * P[L-i-1]
        
        return ans + 1

        
