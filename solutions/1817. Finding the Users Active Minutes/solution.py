# Problem: Finding the Users Active Minutes
# Language: python3
# Runtime: 1392 ms
# Memory: 24.8 MB

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        g = defaultdict(set)
        N = len(logs)
        for u,v in logs:
            g[u].add(v)
        
        c = Counter()
        
        for u in g:
            c[len(g[u])] += 1
        ans = []
        for i in range(1,k+1):
            ans.append(c[i])
        
        return ans
        
        
            