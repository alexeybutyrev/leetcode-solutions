# Problem: Minimum Number of Operations to Make Word K-Periodic
# Language: python3
# Runtime: 136 ms
# Memory: 18.8 MB

class Solution:
    def minimumOperationsToMakeKPeriodic(self, S: str, K: int) -> int:
        c = Counter()
        N = len(S)
        
        for i in range(0,N,K):
            c[S[i:i+K]] += 1
        
        v = c.values()
        
        return sum(v) - max(v)