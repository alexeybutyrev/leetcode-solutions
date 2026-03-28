# Problem: Longest Common Subsequence
# Language: python3
# Runtime: 1388 ms
# Memory: 144.4 MB

from collections import Counter
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = {}
        
        def walk(text1, text2, i, j):
            if i == n1 or j == n2:
                return 0
            if (i,j) not in dp:
                s0 = 0
                if text1[i] == text2[j]:
                    s0 = 1 + walk(text1, text2, i+1,j+1)

                s1 = walk(text1, text2, i+1, j)
                s2 = walk(text1, text2, i, j+1)

                dp[(i,j)] = max(s0, s1, s2)
            return dp[(i,j)]
        
            
            
        return walk(text1, text2,0,0)
            