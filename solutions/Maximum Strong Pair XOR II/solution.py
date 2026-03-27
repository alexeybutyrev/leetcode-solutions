# Problem: Maximum Strong Pair XOR II
# Language: python3
# Runtime: 8676 ms
# Memory: 125.3 MB

class Trie:
    def __init__(self, size=22):
        self.size = size
        self.t = defaultdict(Trie)
        self.count = 0
    
    def add(self, n):
        trie  = self
        trie.count +=1
        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            trie = trie.t[bit]
            trie.count += 1
            
    def delete(self, n):
        trie  = self
        trie.count -=1
        for i in range(self.size, -1, -1):
            bit = bool(n & (1 << i))
            trie = trie.t[bit]
            trie.count -= 1
                
    def max_xor(self, n):
        trie = self
        xor = 0
        
        for i in range(self.size, -1,-1):
            bit = bool(n & (1 << i))
            if 1 - bit in trie.t and trie.t[1-bit].count:
                xor |= (1 << i)
                trie = trie.t[1- bit]
            else:
                trie = trie.t[bit]
        
        return xor
    
class Solution:
    def maximumStrongPairXor(self, A: List[int]) -> int:
        A.sort()
        t = Trie()
        
        stack = deque()
        ans = 0
        for y in A:
            if stack:
                while stack and stack[0] < y - stack[0]:
                    x = stack.popleft()
                    t.delete(x)
                if stack:
                    ans = max(ans, t.max_xor(y))
            stack.append(y)
            t.add(y)
        return ans
    
    
    