# Problem: Time Based Key-Value Store
# Language: python3
# Runtime: 661 ms
# Memory: 70.6 MB

class TimeMap:

    def __init__(self):
        self.kt = defaultdict(list)
        self.k = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kt[key].append(timestamp)
        self.k[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not self.kt[key]:
            return ""
        ind = bisect_right(self.kt[key], timestamp)
        if ind == 0 and self.kt[key][0] > timestamp:
            return ""
        
        ind -= 1
        
        ts = self.kt[key][ind]

        return self.k[key][ts]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)