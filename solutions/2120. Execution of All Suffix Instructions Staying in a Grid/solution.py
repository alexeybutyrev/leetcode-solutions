# Problem: Execution of All Suffix Instructions Staying in a Grid
# Language: python3
# Runtime: 2266 ms
# Memory: 436 MB

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        @cache
        def dfs(i,j,k):
            if i == n or j == n or i < 0 or j < 0 or k == len(s):
                return 0
            if s[k] == "R":
                if j + 1 < n:
                    return 1 + dfs(i,j+1,k+1)
                else:
                    return 0
                
            if s[k] == "L":
                if j - 1 >= 0:
                    return 1 + dfs(i,j-1,k+1)
                else:
                    return 0
                
            if s[k] == "U":
                if i - 1 >= 0:
                    return 1 + dfs(i-1,j,k+1)
                else:
                    return 0
            if i + 1 < n:
                return 1 + dfs(i+1,j,k+1)
            else:
                return 0
        

        ans = []
        for k in range(len(s)):
            ans.append(dfs(startPos[0],startPos[1],k))
        return ans