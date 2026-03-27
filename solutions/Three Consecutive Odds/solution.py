# Problem: Three Consecutive Odds
# Language: python3
# Runtime: 53 ms
# Memory: 16.6 MB

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any( k and (len(list(v))>2) for k, v in groupby([x&1 for x in  arr]))