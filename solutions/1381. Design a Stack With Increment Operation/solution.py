# Problem: Design a Stack With Increment Operation
# Language: python3
# Runtime: 89 ms
# Memory: 17.6 MB

class CustomStack:

    def __init__(self, maxSize: int):
        self.A = []
        self.N = maxSize

    def push(self, x: int) -> None:
        if len(self.A) < self.N:
            self.A.append(x)

    def pop(self) -> int:
        if not self.A:
            return -1
        return self.A.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.A),k)):
            self.A[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)