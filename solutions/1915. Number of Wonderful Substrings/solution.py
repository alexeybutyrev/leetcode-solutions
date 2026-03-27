# Problem: Number of Wonderful Substrings
# Language: python3
# Runtime: 1980 ms
# Memory: 17.5 MB

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = curr = 0
        c = Counter()
        c[0] = 1
        for x in word:
            curr ^= (1 << (ord(x) - ord('a')))
            ans += c[curr]
            c[curr] +=1
            for j in range(10):
                ans += c[curr ^ (1 << j)]
        return ans