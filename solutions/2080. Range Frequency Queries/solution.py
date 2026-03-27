# Problem: Range Frequency Queries
# Language: python3
# Runtime: 2154 ms
# Memory: 53.2 MB

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.C = defaultdict(list)
        for i,a in enumerate(arr):
            self.C[a].append(i)

    def query(self, left: int, right: int, a: int) -> int:
        
        L = bisect.bisect_left(self.C[a], left)
        R = bisect.bisect_right(self.C[a], right)
        return R - L
    


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)