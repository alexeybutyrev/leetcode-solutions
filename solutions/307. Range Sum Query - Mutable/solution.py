# Problem: Range Sum Query - Mutable
# Language: python3
# Runtime: 351 ms
# Memory: 36.1 MB

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def sum(self, i):
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def update(self, i, delta):
        i += 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i
            
class NumArray:

    def __init__(self, A: List[int]):
        self.t = FenwickTree(len(A))
        self.A = A
        for i,x in enumerate(A):
            self.t.update(i,x)
        
    def update(self, i: int, val: int) -> None:
        delta = val - self.A[i]
        self.A[i] = val
        self.t.update(i, delta)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.t.sum(right) - self.t.sum(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)