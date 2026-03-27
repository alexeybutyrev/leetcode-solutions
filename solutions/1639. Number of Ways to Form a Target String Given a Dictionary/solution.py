# Problem: Number of Ways to Form a Target String Given a Dictionary
# Language: python3
# Runtime: 1623 ms
# Memory: 21.2 MB

from sortedcontainers import SortedSet
class Solution:
    def numWays(self, words: List[str], T: str) -> int:
        
        N = len(T)
        M = len(words[0])
  
        ans = [1] + [0] * N
        
        MOD = 10**9 + 7
        for i in range(M):
            c = Counter([w[i] for w in words])    
            for j in range(N-1,-1,-1):
                ans[j+1] += ans[j] * c[T[j]]
        return ans[N] % MOD