# Problem: Strobogrammatic Number II
# Language: python3
# Runtime: 200 ms
# Memory: 29.8 MB

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        c = ["0","1","8"]
        
        if n == 1:
            return c
        
        mapping = {"0":"0",
                   "1":"1",
                   "6":"9",
                   "9":"6",
                   "8":"8"}
        
        def backtrack(i, s, N):
            if i == N:
                if not s.startswith("0"):
                    ans.append(s)
            else:
                for l in ["0","1","8", "6","9"]:
                    backtrack(i+1,l + s + mapping[l], N )
        
                
        ans = []
        if n % 2 == 0:
            
            N = n // 2
            backtrack(0, "", N)
        else:
            n -= 1
            N = n // 2
            for l in c:
                backtrack(0, l, N)
        
        return ans
                        