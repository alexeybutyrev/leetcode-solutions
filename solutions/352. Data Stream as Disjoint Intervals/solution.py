# Problem: Data Stream as Disjoint Intervals
# Language: python3
# Runtime: 2756 ms
# Memory: 19.9 MB

class SummaryRanges:

    def __init__(self):
        self.UF = {}
        self.seen = set()
    
    def find(self, x):
        if x != self.UF[x]:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]
    
    def union(self, x,y):
        self.UF.setdefault(x,x)
        self.UF.setdefault(y,y)
        self.UF[self.find(x)] = self.find(y)
        

    def addNum(self, val: int) -> None:
        self.union(val, val)
        if val + 1 in self.seen:
            self.union(val+1,val)
        
        if val - 1 in self.seen:
            self.union(val-1,val)
        
        self.seen.add(val)

    def getIntervals(self) -> List[List[int]]:
        mins = defaultdict(lambda: inf)
        maxs = defaultdict(lambda: -inf)
        for i in self.seen:
            p = self.find(i)
            mins[p] = min(i,mins[p])
            maxs[p] = max(i,maxs[p])
        
        ans = []
        for p in mins:
            ans.append([mins[p],maxs[p]])
        ans.sort()
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()