# Problem: Successful Pairs of Spells and Potions
# Language: python3
# Runtime: 1234 ms
# Memory: 37.3 MB

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        return [N - bisect_left(potions,success/s) for s in spells]