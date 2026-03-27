# Problem: Shortest Word Distance II
# Language: python3
# Runtime: 123 ms
# Memory: 22 MB

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.d[w].append(i)
    def shortest(self, word1: str, word2: str) -> int:
        N1 = len(self.d[word1])
        N2 = len(self.d[word2])
        i = j = 0
        ans = inf
        while i < N1 and j < N2:
            ans = min(ans, abs(self.d[word1][i] - self.d[word2][j]))
            if self.d[word1][i] < self.d[word2][j]:
                i+=1
            else:
                j+=1
                
        return ans
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)