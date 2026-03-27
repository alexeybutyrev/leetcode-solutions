# Problem: Count the Number of Consistent Strings
# Language: python3
# Runtime: 231 ms
# Memory: 18.9 MB

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        ans = 0
        for w in  words:
            if not (set(w) -s):
                ans+=1
        return ans