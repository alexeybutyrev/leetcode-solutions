# Problem: Shortest Word Distance III
# Language: python3
# Runtime: 733 ms
# Memory: 37.1 MB

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        A = []
        B = []
        for i,w in enumerate(wordsDict):
            if w == word1:
                A.append(i)
            elif w == word2:
                B.append(i)
        
        ans = inf
        if word1 == word2:
            for i in range(len(A)-1):
                ans = min(ans, A[i+1] - A[i])
            return ans
        
        i = j = 0
        while i < len(A) and j < len(B):
            ans = min(ans,abs(A[i] - B[j]))
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
        
        return ans