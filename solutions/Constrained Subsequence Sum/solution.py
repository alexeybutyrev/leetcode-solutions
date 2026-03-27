# Problem: Constrained Subsequence Sum
# Language: python3
# Runtime: 780 ms
# Memory: 27.5 MB

class Monoque(deque):
    
    def enque(self, val):
        count = 1
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])
    
    def deque(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        
        return ans
        
    def max(self):
        if self:
            return self[0][0]
        else:
            return 0
    
class Solution:
    def constrainedSubsetSum(self, A: List[int], K: int) -> int:
        monoq = Monoque()
        ans = max(A)
        for i,x in enumerate(A):
            monoq.enque(x + max(0,monoq.max()))
            
            if i >= K:
                ans = max(ans, monoq.deque())
        return ans