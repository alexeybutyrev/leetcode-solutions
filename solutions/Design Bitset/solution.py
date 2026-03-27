# Problem: Design Bitset
# Language: python3
# Runtime: 1354 ms
# Memory: 58.2 MB

class Bitset:

    def __init__(self, size: int):
        self.N = size
        self.curr   = {}
        self.fliped = {i: 1 for i in range(size)}
        self.f = False
        
    def fix(self, idx: int) -> None:
        if self.f:
            if idx in self.curr:
                del self.curr[idx]
            
            self.fliped[idx] = 1
        else:
            if idx in self.fliped:
                del self.fliped[idx]
            self.curr[idx] = 1
            
        
    def unfix(self, idx: int) -> None:
        if not self.f:
            if idx in self.curr:
                del self.curr[idx]
            
            self.fliped[idx] = 1
        else:
            if idx in self.fliped:
                del self.fliped[idx]
            self.curr[idx] = 1
        
    def flip(self) -> None:
        self.f = not self.f

    def all(self) -> bool:
        if self.f:
            return len(self.fliped) == self.N
        else:
            return len(self.curr) == self.N
        
    

    def one(self) -> bool:
        if self.f:
            return len(self.fliped) > 0
        else:
            return len(self.curr) > 0

    def count(self) -> int:
        if self.f:
            return len(self.fliped)
        else:
            return len(self.curr)
        

    def toString(self) -> str:
        ans = ''
        if self.f:
            for i in range(self.N):
                if i in self.fliped:
                    ans = ans + '1'
                else:
                    ans = ans + '0'
        else:
            for i in range(self.N):
                if i in self.curr:
                    ans = ans + '1'
                else:
                    ans = ans + '0'
        return ans


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()