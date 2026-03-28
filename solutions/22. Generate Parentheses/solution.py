# Problem: Generate Parentheses
# Language: python3
# Runtime: 48 ms
# Memory: 14.7 MB

class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        ans = set()
        N = 2 *N 
        def dfs(i,s,n):
            if n >= 0:
                if i == N and n == 0:
                    ans.add(s)
                if i < N:
                    for p, c in zip(["(",")"],[1,-1]):
                        dfs(i+1, s + p, n + c)
        
        dfs(0,"",0)
        return ans
                    