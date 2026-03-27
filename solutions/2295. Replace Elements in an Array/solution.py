# Problem: Replace Elements in an Array
# Language: python3
# Runtime: 2434 ms
# Memory: 85.1 MB

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hm = defaultdict(set)
        for i,x in enumerate(nums):
            hm[x].add(i)
        
        for u,v in operations:
            if u not in hm:
                continue
            hm[v] |= hm[u]
            del hm[u]
        
        ans = [0] * len(nums)
        for k,v in hm.items():
            for x in v:
                ans[x] = k
        
        return ans