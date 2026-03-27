# Problem: Online Majority Element In Subarray
# Language: python3
# Runtime: 1158 ms
# Memory: 27.5 MB

class MajorityChecker:

    def __init__(self, A: List[int]):
        self.A = A
        self.N = len(A)
        
        self.d = defaultdict(list)
        
        for i,x in enumerate(A):
            self.d[x].append(i)
            
            
    def query(self, left: int, right: int, threshold: int) -> int:
        
        for _ in range(20):
            a = self.A[random.randint(left, right)]
            lo = bisect_left(self.d[a], left)
            hi = bisect_right(self.d[a], right)
            if hi -lo >= threshold:
                return a
        return -1
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)