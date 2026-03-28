# Problem: Minimum Time to Type Word Using Special Typewriter
# Language: python3
# Runtime: 41 ms
# Memory: 14.2 MB

class Solution:
    def minTimeToType(self, word: str) -> int:
        
        ans = 0
        curr = 0
        for l in word:
            ind = ord(l) - ord('a')
            delta1 = abs(ind - curr)
            delta2 = 26 - delta1
            ans += min(delta1, delta2)
            ans += 1
            curr = ind
        return ans
            