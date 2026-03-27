# Problem: Destroy Sequential Targets
# Language: python3
# Runtime: 1339 ms
# Memory: 31.1 MB

class Solution:
    def destroyTargets(self, A: List[int], k: int) -> int:
        c = Counter()
        
        for a in A:
            c[a%k] += 1
        
        V = max(c.values())
        ans = inf
        for a in A:
            if c[a %k] == V:
                ans =min(ans,a)
        return ans
            
            