# Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
# Language: python3
# Runtime: 68 ms
# Memory: 15.3 MB

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(n))