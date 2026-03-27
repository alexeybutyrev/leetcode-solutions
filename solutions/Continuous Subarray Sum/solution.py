# Problem: Continuous Subarray Sum
# Language: python3
# Runtime: 852 ms
# Memory: 36.2 MB

class Solution:
    def checkSubarraySum(self, A: List[int], k: int) -> bool:
        N = len(A)
        if N < 2:
            return False
        d = {0: -1}
        s = 0
        for i,x in enumerate(A):
            
            s += x
            if  (s % k) in d:
                if i - d[s%k] > 1:
                    return True
            if s %k not in d:
                d[s%k] = i
        return False