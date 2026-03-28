# Problem: Maximum Number of Balloons
# Language: python3
# Runtime: 32 ms
# Memory: 14.5 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        ans = inf
        for l in {'b','a','n'}:
            ans = min(ans,c[l])
        
        for l in {'o','l'}:
            ans = min(ans,c[l]//2)
        
        return ans
        