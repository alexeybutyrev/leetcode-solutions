# Problem: Defuse the Bomb
# Language: python3
# Runtime: 7 ms
# Memory: 16.9 MB

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        
        
        if k < 0:
            for i in range(n):
                for j in range(i-1,i+k-1,-1):
                    ind = j if j >= 0 else n+j
                    res[i] += code[ind]
        
        else:
            for i in range(n):
                for j in range(i+1,i+k+1):
                    res[i] += code[j%n]
        
        
        return res