# Problem: Minimum Consecutive Cards to Pick Up
# Language: python3
# Runtime: 846 ms
# Memory: 33.8 MB

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        seen = {}
        ans = inf
        for i,c in enumerate(cards):
            if c in seen:
                ans = min(ans, i - seen[c] + 1)
            
            seen[c] = i 
        
        return -1 if ans == inf else ans