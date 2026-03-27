# Problem: Maximum Split of Positive Even Integers
# Language: python3
# Runtime: 504 ms
# Memory: 26.8 MB

class Solution:
    def maximumEvenSplit(self, S: int) -> List[int]:
        if S & 1:
            return []
        
        ans = []
        
        for x in range(2, 10**10,2):
            if x <= S:
                ans.append(x)
                S -= x
            else:
                ans[-1] += S
                break
        
        return ans