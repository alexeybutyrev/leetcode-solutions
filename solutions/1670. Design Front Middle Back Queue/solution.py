# Problem: Design Front Middle Back Queue
# Language: python3
# Runtime: 96 ms
# Memory: 14.9 MB

from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back  = deque()
        
    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        
        if len(self.front) > len(self.back)+1:
            self.back.appendleft(self.front.pop())
        
        #print("pf",self.front,self.back)
        
    def pushMiddle(self, val: int) -> None:
        #print("before pm", val ,self.front,self.back)
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
            
            self.front.append(val)
            
        elif len(self.front) <= len(self.back):
            self.front.append(val)
        
        #print("pm",self.front,self.back)

    def pushBack(self, val: int) -> None:
        self.back.append(val)        
        if len(self.back) > len(self.front)+1:
            self.front.append(self.back.popleft())
        
        #print("pb",self.front,self.back)
        
    def popFront(self) -> int:
        #print("pof",self.front,self.back)
        if self.front:
            v =  self.front.popleft()
            if len(self.back) > len(self.front)+1:
                self.front.append(self.back.popleft())
            return v
        else:
            if self.back:
                return self.back.popleft()
            else:
                return -1
        
    
    def popMiddle(self) -> int:
        #print("pom",self.front,self.back)
        if len(self.front) == len(self.back) ==0:
            return -1
        
        if len(self.front) >= len(self.back):
            v =  self.front.pop()
            if len(self.back) > len(self.front)+1:
                self.front.append(self.back.popleft())
            return v
        
        else:
            return self.back.popleft()
        
        

    def popBack(self) -> int:
        #print("pob",self.front,self.back)
        if self.back:
            v =  self.back.pop()
            if len(self.front) > len(self.back)+1:
                self.back.appendleft(self.front.pop()) 
            return v
        else:
            if self.front:
                return self.front.popleft()
            else:
                return -1
        
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()