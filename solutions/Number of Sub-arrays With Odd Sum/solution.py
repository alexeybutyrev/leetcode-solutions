# Problem: Number of Sub-arrays With Odd Sum
# Language: python3
# Runtime: 43 ms
# Memory: 22.1 MB

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        o,e = 0,1
        count = s = 0
        MOD = 10**9 + 7
        for x in arr:
            s += x
            if s & 1:
                count += e
                o += 1
            else:
                count += o
                e += 1
                
        return count % MOD 
        
