# Problem: Count Nodes With the Highest Score
# Language: python3
# Runtime: 1292 ms
# Memory: 130.8 MB

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def countHighestScoreNodes(self, A: List[int]) -> int:
        N = len(A)
        g = defaultdict(list)
        for i in range(N):
            g[A[i]].append(i)
        
        s = [1] * N
        c = Counter()
        def dfs(x):
            p = 1
            for n in g[x]:
                dfs(n)
                s[x] += s[n]
                p *= s[n]
            
            if x:
                p *= N - s[x]
            
            c[p] += 1
        
        dfs(0)

        return max((k,v) for k,v in c.items())[1]
    
            