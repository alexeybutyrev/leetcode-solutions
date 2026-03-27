# Problem: Capitalize the Title
# Language: python3
# Runtime: 32 ms
# Memory: 14.4 MB

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for w in title.split(" "):
            ans.append(w.lower().capitalize() if len(w) > 2 else w.lower())
        return " ".join(ans)