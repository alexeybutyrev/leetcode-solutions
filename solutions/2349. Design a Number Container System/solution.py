# Problem: Design a Number Container System
# Language: python3
# Runtime: 324 ms
# Memory: 100.1 MB


from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.numbers = defaultdict(SortedList)
        self.inds = {}

    def change(self, index: int, number: int) -> None:
        if index in self.inds:
            num = self.inds[index]    
            self.numbers[num].remove(index)

        self.numbers[number].add(index)
        self.inds[index] = number

    def find(self, number: int) -> int:
            return self.numbers[number][0] if self.numbers[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)