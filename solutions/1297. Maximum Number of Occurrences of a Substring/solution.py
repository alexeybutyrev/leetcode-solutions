# Problem: Maximum Number of Occurrences of a Substring
# Language: python3
# Runtime: 1124 ms
# Memory: 125.8 MB

class Solution:
    def maxFreq(self, S: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        c = Counter()
        
        for i in range(len(S)):
            nl = set()
            for j in range(i, min(len(S), i + maxSize)):
                nl.add(S[j])
                if len(nl) > maxLetters:
                    break
                if j - i >= minSize-1:
                    c[S[i:j+1]] += 1
        return max(c.values()) if c else 0