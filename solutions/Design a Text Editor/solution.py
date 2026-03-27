# Problem: Design a Text Editor
# Language: python3
# Runtime: 1290 ms
# Memory: 28 MB

import re
class TextEditor:

    def __init__(self):
        self.b = ""
        self.a = ""
        self.ind = 0

    def addText(self, text: str) -> None:
        self.b = self.b + text
        #print("add", self.b, self.a)
        
    def deleteText(self, k: int) -> int:
        if len(self.b) <k:
            x = len(self.b)
            self.b = ""
            #print("dell ins", self.b, self.a)
            return x
        
        self.b = self.b[:-k]
        #print("dell out->", self.b, self.a)
        return k
    
    def cursorLeft(self, k: int) -> str:
        if len(self.b) <k:
            self.a = self.b + self.a
            self.b = ""
        else:
            self.a = self.b[-k:] + self.a
            self.b = self.b[:-k]
        #print("left", self.b, self.a)
        return (self.b)[-min(10,len(self.b) ):]
    
    
    def cursorRight(self, k: int) -> str:
        if len(self.a) <= k:
            self.b = self.b + self.a
            self.a = ""
        else:
            #print("here",self.b,self.a)
            self.b = self.b + self.a[:k]
            self.a = self.a[k:]
        #print("right", self.b, self.a, (self.a + self.b)[-min(10,len(self.a) + len(self.b) ):])
        return (self.b)[-min(10,len(self.b) ):]
    

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)