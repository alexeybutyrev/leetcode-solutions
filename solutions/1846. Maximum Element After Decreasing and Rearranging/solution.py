# Problem: Maximum Element After Decreasing and Rearranging
# Language: python3
# Runtime: 534 ms
# Memory: 27.3 MB

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        h = []
        for x in arr:
            heappush(h,x)
        
        ans = []
        curr = 1
        while h:
            x = heappop(h)
            curr = min(curr, x)
            ans.append(curr)
            curr += 1
        return ans[-1]
            