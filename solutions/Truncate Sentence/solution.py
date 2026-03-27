# Problem: Truncate Sentence
# Language: python3
# Runtime: 48 ms
# Memory: 14 MB

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        ans = s[0]
        for i in range(1,k):
            ans += " " + s[i]
        
        return ans