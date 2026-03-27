# Problem: K-diff Pairs in an Array
# Language: python3
# Runtime: 72 ms
# Memory: 15.5 MB

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        
        if k == 0:
            c = Counter(nums)
            count = 0
            for k,v in c.items():
                if v > 1:
                    count += 1
            return count
            
        
        s = set(nums)
        count = 0
        for n in s:
            if n + k in s:
                count += 1
        return count