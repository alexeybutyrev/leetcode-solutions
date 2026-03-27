# Problem: Hand of Straights
# Language: python3
# Runtime: 543 ms
# Memory: 17.9 MB

class Solution:
    def isNStraightHand(self, hand: List[int], K: int) -> bool:
        c = Counter(hand)
        
        if len(hand) % K != 0:
            return False
        
        while c:
            curr = min(c.keys())
            
            for x in range(curr, curr + K):
                if x not in c:
                    return False
                c[x] -= 1
                if not c[x]:
                    del c[x]
        return True
        