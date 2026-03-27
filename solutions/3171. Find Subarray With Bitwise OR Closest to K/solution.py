# Problem: Find Subarray With Bitwise OR Closest to K
# Language: python3
# Runtime: 1295 ms
# Memory: 31.4 MB

class Solution:
    def minimumDifference(self, arr: List[int], target: int) -> int:
        
        ans, seen = inf, set()
        for a in arr:
            seen = {ss & a for ss in seen } | {a}
            ans = min(ans, min(abs(x - target) for x in seen))
        
        return ans
    