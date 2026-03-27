# Problem: Find a Value of a Mysterious Function Closest to Target
# Language: python3
# Runtime: 962 ms
# Memory: 27 MB

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        
        ans, seen = inf, set()
        for a in arr:
            seen = {ss & a for ss in seen } | {a}
            ans = min(ans, min(abs(x - target) for x in seen))
        
        return ans