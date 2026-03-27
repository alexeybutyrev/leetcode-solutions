# Problem: Largest Divisible Subset
# Language: python3
# Runtime: 171 ms
# Memory: 17.4 MB

class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        ss = {-1: set()}
        
        for n in sorted(A):
            ss[n] = max( [ss[x] for x in ss if n % x == 0], key = len ) | {n}
        
        return max(ss.values(), key = len)
            
                    