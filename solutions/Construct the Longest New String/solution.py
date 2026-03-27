# Problem: Construct the Longest New String
# Language: python3
# Runtime: 3430 ms
# Memory: 181 MB

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        self.ans = 0
        @cache
        def dfs(x,y,z,curr,FINAL):
            self.ans = max(self.ans, FINAL)
            ans = 0
            if curr == '':
                if x:
                    ans += dfs(x - 1, y, z, 'x',FINAL + 2)
                if y:
                    ans += dfs(x, y-1, z, 'y',FINAL + 2)
                if z:
                    ans += dfs(x, y, z-1, 'z',FINAL + 2)
            elif curr == 'x':
                if x:
                    ans += 0
                    
                if y:
                    ans += dfs(x, y-1, z, 'y',FINAL + 2)
                    
                if z:
                    ans += 0
                    
            elif curr == 'y':
                if x:
                    ans += dfs(x - 1, y, z, 'x',FINAL + 2)
                    
                if y:
                    ans += 0
                
                if z:
                    ans += dfs(x, y, z-1, 'z',FINAL + 2)
            
            else:
                if x:
                    ans += dfs(x - 1, y, z, 'x',FINAL + 2)
                if y:
                    ans += 0
                if z:
                    ans += dfs(x, y, z-1, 'z',FINAL + 2)
            
            return ans
        
        dfs(x,y,z,'', 0)
        return self.ans
                