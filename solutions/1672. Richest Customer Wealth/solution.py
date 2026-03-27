# Problem: Richest Customer Wealth
# Language: python3
# Runtime: 48 ms
# Memory: 13.8 MB

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max( sum(a) for a in accounts)