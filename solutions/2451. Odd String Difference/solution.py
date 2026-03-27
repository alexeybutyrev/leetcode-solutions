# Problem: Odd String Difference
# Language: python3
# Runtime: 67 ms
# Memory: 13.9 MB

class Solution:
    def oddString(self, words: List[str]) -> str:
        N = len(words)
        W = []
        n = len(words[0])
        for w in words:
            d = []
            for l in w:
                d.append(ord(l) - ord('a'))
            W.append(d)
        difference = []
        for i in range(N):
            d = []
            for j in range(n-1):
                d.append(W[i][j+1] - W[i][j])
            difference.append(d)
        
        seen = defaultdict(list)
        for i in range(N):
            seen[tuple(difference[i])].append(i)
        #print(seen)
        for k in seen:
            if len(seen[k]) == 1:
                return words[seen[k][0]]