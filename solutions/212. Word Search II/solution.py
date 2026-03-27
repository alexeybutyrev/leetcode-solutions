# Problem: Word Search II
# Language: python3
# Runtime: 3772 ms
# Memory: 14.6 MB

class Trie:
    def __init__(self):
        self.children = {}
        
    def add(self, word):
        if not self.children:
            self.children[""] = {}
            
        curr = self.children[""]
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr["$"] = word
class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        
        T = Trie()
        for w in words:
            T.add(w)
        
        
        ans = set()
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        
        def dfs(i, j, seen, d):
            if "$" in d:
                ans.add(d["$"])
                
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < N and x >= 0 and y >= 0 and y < M and (x,y) not in seen and (A[x][y] in d):
                    dfs(x, y, seen | {(x,y)}, d[A[x][y]])
                    
        
        N, M = len(A), len(A[0])
        for i in range(N):
            for j in range(M):
                if len(ans) == len(words):
                    return ans
                if A[i][j] in T.children[""]:
                    dfs(i,j, {(i,j)}, (T.children[""])[A[i][j]])
        
        return ans
                    