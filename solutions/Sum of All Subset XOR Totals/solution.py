# Problem: Sum of All Subset XOR Totals
# Language: python3
# Runtime: 15 ms
# Memory: 17.7 MB

from itertools import combinations
class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        ans = 0
        for i in range(1, len(A) + 1):
            
            for c in combinations(A, i):
                s = 0
                for e in c:
                    s ^= e
                ans += s
                
        return ans