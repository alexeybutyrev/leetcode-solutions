# Problem: Word Subsets
# Language: python3
# Runtime: 1250 ms
# Memory: 21.3 MB

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = set(["".join(sorted(w)) for w in words2])
        C = list()
        for w in words2:
            C.append(Counter(w))
            
        ans = []
        for w in words1:
            c = Counter(w)
            pr = True
            for c2 in C:
                for x in c2:
                    if c2[x] > c[x]:
                        pr = False
                        break
                if not pr:
                    break
            else:
                ans.append(w)
                
        return ans