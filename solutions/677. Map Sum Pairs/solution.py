# Problem: Map Sum Pairs
# Language: python3
# Runtime: 28 ms
# Memory: 14.3 MB

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.val = 0
        
    def add(self, word, val):
        delta = self.searh(word)
        val -= delta
        curr = self
        for l in word:
            curr = curr.children[l]
            curr.val += val
        
        curr = curr.children['$']
        curr.val += val
    
    def searh(self, word):
        node = self
        for l in word:
            if l not in node.children:
                return 0
            node = node.children[l]
        if '$' in node.children:
            return node.children['$'].val
        
        return 0
    
    def find_prefix(self, prefix):
        node = self
        for l in prefix:
            if l not in prefix:
                return 0
            node = node.children[l]
        return node.val
            
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Node()

    def insert(self, key: str, val: int) -> None:
        self.t.add(key,val)

    def sum(self, prefix: str) -> int:
        return self.t.find_prefix(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)