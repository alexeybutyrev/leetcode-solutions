# Problem: Largest Divisible Subset
# Language: python3
# Runtime: 135 ms
# Memory: 18.7 MB

class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        ss = {-1: set()}
        
        for n in sorted(A):
            ss[n] = max( [ss[x] for x in ss if n % x == 0], key = len ) | {n}
        
        return list(max(ss.values(), key = len))