# Problem: Ways to Split Array Into Good Subarrays
# Language: python3
# Runtime: 2396 ms
# Memory: 20.3 MB

class Solution:
    def numberOfGoodSubarraySplits(self, A: List[int]) -> int:
        for i,x in enumerate(A):
            if x == 1:
                break
        else:
            return 0
        
        MOD = 10 ** 9 + 7
        n = 1
        count = 1
        for i in range(i+1,len(A)):
            if A[i] == 0:
                count += 1
            else:
                n *= count
                n %= MOD
                count = 1
                
        return n