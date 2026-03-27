# Problem: Lexicographically Smallest String After Reverse
# Language: python3
# Runtime: 1110 ms
# Memory: 18.1 MB

class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = 'z' * len(s)
        S = list(s)
        for k in range(1,len(s)+1):
            s1 = S[:k][::-1] + S[k:]
            ans = min(ans,"".join(s1))
            s1 = S[:-k] + S[-k:][::-1]
            ans = min(ans,"".join(s1))
            
        return ans