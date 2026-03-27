# Problem: Implement Stack using Queues
# Language: python3
# Runtime: 35 ms
# Memory: 13.9 MB

class MyStack:

    def __init__(self):
        self.A = []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        return self.A.pop()

    def top(self) -> int:
        return self.A[-1]

    def empty(self) -> bool:
        return self.A == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()