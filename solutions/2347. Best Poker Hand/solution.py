# Problem: Best Poker Hand
# Language: python3
# Runtime: 44 ms
# Memory: 13.9 MB

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        c = Counter(suits)
        if len(c) == 1:
            return "Flush"
        r = Counter(ranks)
        v = [v for k,v in r.items()]
        v.sort()
        if v[-1] >= 3:
            return "Three of a Kind"
        if v[-1] == 2:
            return "Pair"
        return "High Card"