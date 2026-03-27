# Problem: Insert Delete GetRandom O(1)
# Language: python3
# Runtime: 346 ms
# Memory: 65.3 MB

from sortedcontainers import SortedList
class RandomizedSet:

    def __init__(self):
        self.A = SortedList()
        
    def insert(self, val: int) -> bool:
        ind = self.A.bisect_left(val)
        if ind < len(self.A) and self.A[ind]==val:
            return False
        self.A.add(val)
        return True

    def remove(self, val: int) -> bool:
        ind = self.A.bisect_left(val)
        if ind < len(self.A) and self.A[ind]==val:
            self.A.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        ind = random.randint(0,len(self.A)-1)
        return self.A[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()