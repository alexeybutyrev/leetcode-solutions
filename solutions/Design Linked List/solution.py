# Problem: Design Linked List
# Language: python3
# Runtime: 182 ms
# Memory: 16.8 MB

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1
        self.size += 1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        nx = curr.next 
        n = Node(val)
        n.next = nx
        curr.next = n
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        self.size -= 1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)