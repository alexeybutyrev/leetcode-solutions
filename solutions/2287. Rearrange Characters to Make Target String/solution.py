# Problem: Rearrange Characters to Make Target String
# Language: python3
# Runtime: 38 ms
# Memory: 13.8 MB

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        ct = Counter(target)
        ans = inf
        for l in ct:
            ans = min(ans,c[l] // ct[l])
        
        return ans