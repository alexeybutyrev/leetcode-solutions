# Problem: Maximum Genetic Difference Query
# Language: python3
# Runtime: 8860 ms
# Memory: 233.8 MB

class Trie:
    def __init__(self, size = 18):
        self._trie = {}
        self.size = size
        self.go = 0
        
    def add(self, n, f = 1):
        trie = self._trie
        
        for i in range(self.size, -1, -1):
            bit = (n >> i) & 1
            trie = trie.setdefault(bit, dict())
            trie[-1] = trie.get(-1, 0) + f
        
    
    def xor(self, n):
        trie = self._trie
        xor = 0
        
        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            desired = 1-bit if 1-bit in trie and trie[1-bit][-1] > 0 else bit
            xor |= (desired ^ bit) << i
            trie = trie[desired]
            
        return xor
    
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        
        Q = defaultdict(list)
        graph = defaultdict(list)
        size = 0
        for i,(node,val) in enumerate(queries):
            Q[node].append((i,val))
            size = max(size, val.bit_length(),i.bit_length())
        
        for i,p in enumerate(parents):
            graph[p].append(i)
        
        trie = Trie(size = size)
        ANS = [-1] * len(queries)
        
        def dfs(node):
            trie.add(node)
            
            for i,val in Q[node]: ANS[i] = trie.xor(val)
            for n in graph[node]: dfs(n)
            
            trie.add(node, -1)
            
        dfs(graph[-1][0])
        
        return ANS