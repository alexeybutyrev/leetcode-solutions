# Problem: Minimum Cost to Set Cooking Time
# Language: python3
# Runtime: 2420 ms
# Memory: 293.6 MB

class Solution:
    def minCostSetTime(self, startAt: int, M: int, P: int, target: int) -> int:
        
        @cache
        def eval_s(s):
            if not s:
                return 0
            if len(s) <=2:
                return int(s)
            return int(s[:-2]) * 60 + int(s[-2:])
        
        @cache
        def dfs(s,at):
            es = eval_s(s)
            if es == target:
                return 0
            
            if len(s) == 4 or es > target:
                return inf
            
            i = len(s)
            ans = inf
            for d in range(10):
                if d != at:
                    ans = min(ans, dfs(s + str(d),d) + M + P)
                else:
                    ans = min(ans, dfs(s + str(d),at) + P)
            return ans
        
        return dfs("",startAt)
    