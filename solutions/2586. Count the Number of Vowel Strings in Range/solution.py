# Problem: Count the Number of Vowel Strings in Range
# Language: python3
# Runtime: 62 ms
# Memory: 14.1 MB

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vovel = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        for w in words[left:right+1]:
            if w[0] in vovel and w[-1] in vovel:
                ans += 1
        return ans