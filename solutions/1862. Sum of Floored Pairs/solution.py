# Problem: Sum of Floored Pairs
# Language: python3
# Runtime: 2116 ms
# Memory: 33.3 MB

class Solution:
    def sumOfFlooredPairs(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        M = max(A)
        count = Counter(A)
        
        vals = [0] * (M + 1)
        
        for x in count:
            for xx in range(x,M+1,x):
                vals[xx] += count[x]
        
        for i in range(1, len(vals)):
            vals[i] += vals[i-1]
        
        return sum(vals[x] for x in A) % MOD
        
                