# Problem: Word Break II
# Language: python3
# Runtime: 30 ms
# Memory: 16.5 MB

class Solution:
    def wordBreak(self, s: str, W: List[str]) -> List[str]:
        N = len(s)
        ans = set()

        def dp(i, t):
            if i >= N:
                xs = []
                for i in t:
                    xs.append(W[i])
                ans.add(" ".join(xs))
            else:
                
                for j, w in enumerate(W):
                    if s[i:].startswith(w):
                        dp(i +len(w), t + tuple([j]))
        
        dp(0,tuple())
        return ans
                        
        
                    