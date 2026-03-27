# Problem: Word Squares II
# Language: python3
# Runtime: 104 ms
# Memory: 26.1 MB

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)

        NW = len(words)

        graphTL = defaultdict(list)
        graphTR = defaultdict(list)

        graphBL = defaultdict(list)
        graphBR = defaultdict(list)

        for i in range(NW):
            for j in range(NW):
                w1 = words[i]
                w2 = words[j]

                if w1[0] == w2[0]:
                    graphTL[i].append(j)
                
                if w1[3] == w2[0]:
                    graphTR[i].append(j)
                
                if w1[0] == w2[3]:
                    graphBL[i].append(j)

                if w1[3] == w2[3]:
                    graphBR[i].append(j)
                
        ans = set()
        for i in graphTL:
            for j in graphBR:
                for l in graphTL[i]:
                    for r in graphTR[i]:
                        if l in graphBL[j] and r in graphBR[j]:
                            if 4 == len(set([i,l,r,j])):
                                ans.add(tuple([words[x] for x in [i,l,r,j]]))

        return sorted(ans)