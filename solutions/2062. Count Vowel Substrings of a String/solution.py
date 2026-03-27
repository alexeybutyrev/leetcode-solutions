# Problem: Count Vowel Substrings of a String
# Language: python3
# Runtime: 232 ms
# Memory: 14.2 MB

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(N:=len(word)):
            for j in range(i+1,N+1):
                s = set(word[i:j])
                if s - v or len(s) < 5:
                    continue
                count += 1
        return count
    