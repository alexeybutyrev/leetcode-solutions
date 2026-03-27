# Problem: Find Maximum Number of String Pairs
# Language: python3
# Runtime: 70 ms
# Memory: 16.2 MB

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i,w in enumerate(words):
            for j in range(i+1,len(words)):
                if words[j] == w[::-1]:
                    ans += 1
        return ans