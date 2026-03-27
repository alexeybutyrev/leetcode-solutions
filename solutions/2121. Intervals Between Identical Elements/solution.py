# Problem: Intervals Between Identical Elements
# Language: python3
# Runtime: 1284 ms
# Memory: 48.6 MB

from itertools import accumulate
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        
        for i,a in enumerate(arr):
            d[a].append(i)
        ans = [0] * len(arr)
        
        for row in d.values():
            left = 0
            right = sum(row)
            for i,ind in enumerate(row):
                right -= ind
                ans[ind] += right - (len(row) - i - 1) * ind
                ans[ind] += i*ind - left
                left += ind
        return ans
                
        #[4,2,7,2,4,4,5]