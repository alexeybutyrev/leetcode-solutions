# Problem: K-th Symbol in Grammar
# Language: python
# Runtime: 20 ms
# Memory: 11.8 MB

class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        if K <= (2**(N-2)):
            return self.kthGrammar(N-1, K)
        return self.kthGrammar(N-1, K - 2**(N-2)) ^ 1