# Problem: Maximum Number of Words You Can Type
# Language: python3
# Runtime: 3 ms
# Memory: 17.8 MB

class Solution:
    def canBeTypedWords(self, text: str, bl: str) -> int:
        b = set(bl)
        ans = 0
        for w in text.split(" "):
            if not set(w) & b:
               ans+=1
        return ans
