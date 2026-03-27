# Problem: Count Paths That Can Form a Palindrome in a Tree
# Language: python3
# Runtime: 2692 ms
# Memory: 160.5 MB

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        S = [ (1 << (ord(x) - ord('a'))) for x in s]
        N = len(parent)
        root = -1
        for i,(u,v) in enumerate(zip(parent, S)):
            if u == -1:
                root = i
            else:
                graph[u].append((i,v))
        
        res = [0] * N
        def walk(node, x = 0):
            
            res[node] = x
            for v,m in graph[node]:
                walk(v, x ^ m)
        
        walk(root)
        targets = {1 << c for c in range(26)}
        targets.add(0)
        c = Counter()
        ans = 0
        for x in res:
            for t in targets:
                ans += c[t^x]
            c[x] += 1
                
        return ans