# Problem: Number of Valid Words for Each Puzzle
# Language: python3
# Runtime: 532 ms
# Memory: 30.2 MB

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        hm = Counter()
        hs = defaultdict(set)
        for w in words:
            mask = 0
            for l in w:
                i = ord(l) - ord('a')
                mask |= (1 << i)
            hm[mask] +=1
        
        seen = {}
        ans = [0] * len(puzzles)
        for i,p in enumerate(puzzles):
            first = 1 << (ord(p[0]) - ord('a'))
            count = hm[first]
            mask = 0
            for l in p[1:]:
                ind = ord(l) - ord('a')
                mask |= (1 << ind)
            
            submask = mask
            while submask:
                count += hm[submask | first]
                submask = (submask-1) & mask
            ans[i] = count
        return ans