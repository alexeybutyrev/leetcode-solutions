# Problem: Maximum XOR of Two Numbers in an Array
# Language: python
# Runtime: 1136 ms
# Memory: 51.7 MB

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
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = Trie(size = max(nums).bit_length())
        
        for n in nums:
            T.add(n)
        
        return max([T.max_xor(n) for n in nums])