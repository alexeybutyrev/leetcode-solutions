# Problem: Maximum XOR With an Element From Array
# Language: python
# Runtime: 6548 ms
# Memory: 466.8 MB

class Trie:
    def __init__(self, size=32):
        self.size = size
        self._trie = {}
    
    def add(self, n):
        trie  = self._trie
        
        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]
    
    def max_xor(self, n):
        trie = self._trie
        xor = 0
        
        for i in range(self.size, -1,-1):
            bit = bool(n & (1 << i))
            if 1 - bit in trie:
                xor |= (1 << i)
                trie = trie[1- bit]
            else:
                trie = trie[bit]
        
        return xor
    
class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        
        T = Trie(30)
        Q = [ (x,m,i) for i, (x,m) in enumerate(queries) ]
        
        Q.sort(key = lambda x: x[1])
        
        i = 0
        N = len(nums)
        ans = [None] * len(Q)
        for x,m, j in Q:
            
            while i < N and nums[i] <= m:
                T.add(nums[i])
                i+=1
            
            ans[j] = T.max_xor(x) if T._trie else -1
            
                
    
        return ans
        
        