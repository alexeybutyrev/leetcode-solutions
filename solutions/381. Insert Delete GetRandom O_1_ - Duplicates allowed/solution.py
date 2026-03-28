# Problem: Insert Delete GetRandom O(1) - Duplicates allowed
# Language: python3
# Runtime: 432 ms
# Memory: 66 MB

from random import choice
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.dind = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.l.append(val)
        self.dind[val].add(len(self.l) - 1)
        return len(self.dind[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dind[val]: return False
        
        remove = self.dind[val].pop()
        last = self.l[-1]
        self.l[remove] = last
        self.dind[last].add(remove)
        self.dind[last].discard(len(self.l) - 1)
        
        self.l.pop()
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.l)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()