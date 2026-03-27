# Problem: Find Players With Zero or One Losses
# Language: python3
# Runtime: 1436 ms
# Memory: 72 MB

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        c = Counter()
        seen = set()
        for w,l in matches:
            c[l] += 1
            seen.add(w)
        
        winners = []
        for x in seen:
            if x not in c:
                winners.append(x)
        loosers = []
        for l in c:
            if c[l] == 1:
                loosers.append(l)
        
        return [sorted(winners), sorted(loosers)]