# Problem: Split Strings by Separator
# Language: python3
# Runtime: 125 ms
# Memory: 16.6 MB

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            ans.extend(w.split(separator))
        return [x for x in ans if x]