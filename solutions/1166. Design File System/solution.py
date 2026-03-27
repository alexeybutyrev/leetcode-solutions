# Problem: Design File System
# Language: python3
# Runtime: 285 ms
# Memory: 21.6 MB

class FileSystem:

    def __init__(self):
        self.hm = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.hm:
            return False
        if path.count("/") > 1:
            parent =  "/".join(path.split("/")[:-1])
            if parent not in self.hm:
                return False
        
        self.hm[path] = value
        return True

    def get(self, path: str) -> int:
        return self.hm.get(path,-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)