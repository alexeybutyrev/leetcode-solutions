# Problem: Finding Pairs With a Certain Sum
# Language: python3
# Runtime: 1652 ms
# Memory: 44.4 MB

class FindSumPairs:

    def __init__(self, A: List[int], B: List[int]):
        self.N1 = len(A)
        self.N2 = len(B)
        self.A = A
        self.B = B
        self.C = Counter()
        for b in self.B:
            self.C[b] += 1
        
        
    def add(self, j: int, val: int) -> None:
        self.C[self.B[j]] -= 1
        self.B[j] += val
        self.C[self.B[j]] += 1
        

    def count(self, tot: int) -> int:
        ans = 0
        for a in self.A:
            ans += self.C[tot - a]
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)