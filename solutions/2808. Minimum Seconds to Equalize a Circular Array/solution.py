# Problem: Minimum Seconds to Equalize a Circular Array
# Language: python3
# Runtime: 618 ms
# Memory: 45.9 MB

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        N = len(nums)
        ans = (N) // 2
        for x in d:
            if len(d[x]) > 1:
                
                la = (N - (d[x][-1] - d[x][0])) // 2
                
                for i in range(1,len(d[x])):
                    la = max(la,(d[x][i] - d[x][i-1]) // 2)
                ans = min(ans, la)
        return ans