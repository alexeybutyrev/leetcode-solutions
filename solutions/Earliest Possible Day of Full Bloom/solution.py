# Problem: Earliest Possible Day of Full Bloom
# Language: python3
# Runtime: 1776 ms
# Memory: 35.2 MB

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = [(g,p) for g,p in zip(growTime, plantTime)]
        
        A.sort(key = lambda x: -x[0])
        
        ans = 0
        curr = 0
        
        for g,p in A:
            ans = max(ans, curr + p + g)
            curr += p
        return ans