# Problem: Find Unique Binary String
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB

class Trie:
    def __init__(self):
        self.t = defaultdict(Trie)
        self.count = 0
    def add(self, num):
        curr = self
        curr.count+= 1
        for d in num:
            curr = curr.t[d]
            curr.count+= 1
class Solution:
    def findDifferentBinaryString(self, A: List[str]) -> str:
        t = Trie()
        for n in A:
            t.add(n)
        
        N = len(A)
        
        q = deque([("",t)])
        
        while q:
            val, curr = q.popleft()
            
            for x in ["0","1"]:
                c = curr.t[x]
                if c.count == 0:
                    return val + x + "0" * (N - len(val) - 1)
                q.append((val + x, c))
                