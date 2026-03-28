# Problem: Single-Row Keyboard
# Language: python3
# Runtime: 52 ms
# Memory: 14.5 MB

class Solution:
    def calculateTime(self, S: str, W: str) -> int:
        N = len(S)
        
        hm = {}
        
        for i in range(N):
            for j in range(i,N):
                
                hm[(S[i],S[j])] = abs(i-j)
                hm[(S[j],S[i])] = abs(i-j)
        
        d = 0
        W = S[0] + W
        for i in range(1, len(W)):
            
            d += hm[(W[i-1], W[i])]
        return d