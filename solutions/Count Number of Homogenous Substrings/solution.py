# Problem: Count Number of Homogenous Substrings
# Language: python3
# Runtime: 175 ms
# Memory: 17.5 MB

class Solution:
    def countHomogenous(self, S: str) -> int:
        count = 1
        ans = 0
        MOD = 10**9 + 7
        for i,x in enumerate(S):    
            if i and S[i] == S[i-1]:
                count += 1
                count %= MOD
            else:
                count = 1
                
            ans += count
            ans %= MOD
        
        return ans
    
    