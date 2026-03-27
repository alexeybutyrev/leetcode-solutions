# Problem: Merge Strings Alternately
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N1, N2 = len(word1), len(word2)
        
        ans = ""
        i = j = 0
        while i < N1 and j < N2:
            ans += word1[i] + word2[j]
            i+=1
            j+=1
        
        return ans + word1[i:] + word2[j:]