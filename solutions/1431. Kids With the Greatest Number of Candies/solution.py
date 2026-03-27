# Problem: Kids With the Greatest Number of Candies
# Language: python3
# Runtime: 42 ms
# Memory: 13.9 MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        return [extraCandies + c >= mx for c in candies]