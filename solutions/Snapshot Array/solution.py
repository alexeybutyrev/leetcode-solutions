# Problem: Snapshot Array
# Language: python3
# Runtime: 404 ms
# Memory: 36.6 MB

from copy import deepcopy
from bisect import bisect_left
class SnapshotArray:

    def __init__(self, length: int):
        self.A = defaultdict(int)
        self.s = 0
        self.inds = defaultdict(list)
        pass
        
    def set(self, index: int, val: int) -> None:
        self.A[(self.s, index)] = val
        self.inds[index].append(self.s) 
        
    def snap(self) -> int:
        self.s +=1
        return self.s -1
    
    def get(self, index: int, snap_id: int) -> int:
        if index not in self.inds or self.inds[index][0] > snap_id :
            return 0
        else:
            
            i = bisect.bisect(self.inds[index], snap_id) - 1

            if i == len(self.inds[index]):
                i-=1
            return self.A[(self.inds[index][i], index)]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)