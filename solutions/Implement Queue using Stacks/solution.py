# Problem: Implement Queue using Stacks
# Language: python3
# Runtime: 28 ms
# Memory: 14 MB

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.reverse()
        self.A.append(x)
        self.A.reverse()
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.A.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.A[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.A) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()