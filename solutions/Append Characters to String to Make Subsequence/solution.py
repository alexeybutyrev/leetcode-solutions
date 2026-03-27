# Problem: Append Characters to String to Make Subsequence
# Language: python3
# Runtime: 54 ms
# Memory: 17.7 MB

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N,M,j= len(s),len(t),0
        for x in s:
            if x == t[j]:
                j+=1
                if j == M: return 0
        
        return len(t) -j