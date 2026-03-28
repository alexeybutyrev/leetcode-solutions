# Problem: Expression Add Operators
# Language: python3
# Runtime: 8032 ms
# Memory: 147.1 MB

class Solution:
    def addOperators(self, S: str, T: int) -> List[str]:
        
        N = len(S)
        ans = set()
        @lru_cache(None)
        def dfs(i, t, n):
            if i == N:
                if not (n[0] == "0" and len(n) > 1):
                    if t:
                        for c in ["+", "*", "-", ""]:
                            if c == "" and t and t[-1] == "0":
                                check = t.rstrip("0")
                                if check and check.isdigit():
                                    e = t + c + n
                            else:
                                
                                e = t + c + n
                            if T == eval(e):
                                ans.add(e)
                    else:
                        if int(n) == T:
                            ans.add(n)
            else:
                if n:
                    if not (n[0] == "0" and len(n) > 1):
                        dfs(i, t + "*" + n if t else n, "")
                        dfs(i, t + "+" + n if t else n, "")
                        dfs(i, t + "-" + n if t else n, "")

                dfs(i+1, t, n + S[i])
        
        if not S:
            return []
        
        dfs(1, "", S[0])
        
        return ans
        