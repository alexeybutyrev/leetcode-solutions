# Problem: Design HashMap
# Language: python3
# Runtime: 618 ms
# Memory: 26.4 MB

def eval_key(x):
    return ((x*1031237) & (1<<20) - 1)>>5

class MyHashMap:

    def __init__(self):
        self.A = [ [] for _ in range(1<<15)]
        self.B = [ [] for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        t = eval_key(key)
        if key not in self.A[t]:
            self.A[t].append(key)
            self.B[t].append(value)

    def get(self, key: int) -> int:
        t = eval_key(key)
        if  key in self.A[t]:
            ind = self.A[t].index(key)
            
            return self.B[t][ind]
        else:
            return -1

    def remove(self, key: int) -> None:
        t = eval_key(key)
        if  key in self.A[t]:
            ind = self.A[t].index(key)
            self.A[t].remove(self.A[t][ind])
            self.B[t].remove(self.B[t][ind])
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)