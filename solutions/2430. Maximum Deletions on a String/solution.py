# Problem: Maximum Deletions on a String
# Language: python3
# Runtime: 1587 ms
# Memory: 14.8 MB

class RabiKarp():
    def __init__(self,s):
        self.P = P = 37
        self.MOD = MOD = 10**9 + 7
        Pinv = pow(P,MOD-2,MOD)
        self.pre = pre = [0]
        self.pinvs = pinvs = [1]
        
        ha = 0
        pwr = prwinv = 1
        for i,x in enumerate(map(ord,s)):
            ha = (ha + x * pwr) % MOD
            pwr = pwr * P % MOD
            prwinv = prwinv * Pinv % MOD
            pre.append(ha)
            pinvs.append(prwinv)
    
    def query(self,i,j):
        return (self.pre[j+1] -  self.pre[i]) * self.pinvs[i] % self.MOD

class Solution:
    def deleteString(self, S: str) -> int:
        if len(set(S)) == 1:
            return len(S)
        N = len(S)
        RC = RabiKarp(S)
        
        @cache
        def dp(i):
            ans = 1
            for j in range(i, N):
                i1 = j+1
                j2 = 2 * j - i + 1
                if j2 >= N: break
                if RC.query(i,j) == RC.query(i1,j2):
                    ans = max(ans, 1 + dp(j+1))
            
            return ans
        
        return dp(0)