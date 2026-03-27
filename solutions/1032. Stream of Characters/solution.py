# Problem: Stream of Characters
# Language: python3
# Runtime: 484 ms
# Memory: 38.2 MB


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = {}
        self.stream = deque([])
        for w in set(words):
            curr = self.t
            for l in w[::-1]:
                if l not in curr:
                    curr[l] = {}
                curr = curr[l]
            curr['$'] = {}
            
        

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr = self.t
        for l in self.stream:
            if '$' in curr:
                return True
            if l not in curr:
                return False
            curr = curr[l]
        return '$' in curr
    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)