# Problem: Minimum Length of Anagram Concatenation
# Language: python3
# Runtime: 1188 ms
# Memory: 17.6 MB

class Solution:
    def minAnagramLength(self, S: str) -> int:
        
        c = Counter()
        N = len(S)
        ans = len(S)
        
        for K in range(1,N):
            if N % K == 0:
                CK = Counter(S[0:K])
                for i in range(K,N,K):
                    if Counter(S[i:i+K]) != CK:
                        break
                else:
                    return K

        return ans