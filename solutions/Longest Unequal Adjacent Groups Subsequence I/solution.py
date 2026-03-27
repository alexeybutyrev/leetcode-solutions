# Problem: Longest Unequal Adjacent Groups Subsequence I
# Language: python3
# Runtime: 72 ms
# Memory: 16.3 MB

class Solution:
    def getWordsInLongestSubsequence(self, n: int, A: List[str], G: List[int]) -> List[str]:
        
        c1 = 0
        c2 = 1
        a1 = []
        a2 = []
        for i,g in enumerate(G):
            if g == c1:
                a1.append(A[i])
                c1 ^=1
            if g == c2:
                a2.append(A[i])
                c2 ^= 1
        if len(a1) > len(a2):
            return a1
        return a2