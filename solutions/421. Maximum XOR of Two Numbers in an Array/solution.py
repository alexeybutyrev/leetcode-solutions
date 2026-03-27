# Problem: Maximum XOR of Two Numbers in an Array
# Language: python3
# Runtime: 748 ms
# Memory: 102.6 MB

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        
        
        trie = {}
        
        for n in nums:
            node = trie
            for d in n:
                if d not in node:
                    node[d] = {}
                    
                node = node[d]
                
        max_xor = 0
        for num in nums:
            xor_node = trie
            curr_xor = 0
            for bit in num:
                opp_bit = 1 - bit
                if opp_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[opp_bit]
                else:
                    curr_xor <<= 1
                    xor_node = xor_node[bit]
            
            max_xor = max(max_xor, curr_xor)
        
        return max_xor