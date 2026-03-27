# Problem: Minimum Distance Between Three Equal Elements II
# Language: python3
# Runtime: 391 ms
# Memory: 47.7 MB

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        ans = inf
        for x,l in d.items():
            if len(l) > 2:
                for i in range(2,len(l)):
                    ans = min(ans, abs(l[i]- l[i-1]) +  abs(l[i]- l[i-2]) + abs(l[i-1]- l[i-2]))
        return -1 if ans==inf else ans