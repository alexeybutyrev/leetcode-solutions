# Problem: Two Sum III - Data structure design
# Language: python3
# Runtime: 276 ms
# Memory: 20.4 MB

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        self.pairs = set()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.s:
            self.pairs.add(number)
        else:
            self.s.add(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        
        if len(self.s) < 2 and len(self.pairs) == 0:
            return False
        
        if value % 2 == 0:
            if value // 2 in self.pairs:
                return True

        for e in self.s:
            if value - e in self.s and value -e  != e:
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)