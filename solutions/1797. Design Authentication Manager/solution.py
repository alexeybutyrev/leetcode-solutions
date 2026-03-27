# Problem: Design Authentication Manager
# Language: python3
# Runtime: 420 ms
# Memory: 15.6 MB

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.delta = timeToLive
        self.A = {}
        self.expired = 0
        self.t = 0
        self.cnt = 0
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.A[tokenId] = currentTime
        self.t = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.t != currentTime:
            self.cnt = self.countUnexpiredTokens(currentTime)
            self.t = currentTime
        
        if tokenId in self.A:
            self.A[tokenId] = currentTime
            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        if self.t == currentTime:
            return self.cnt
        
        count = 0
        to_del = set()
        for k,t in self.A.items():
            if t + self.delta > currentTime:
                count += 1  
            else:
                to_del.add(k)
        for e in to_del:
            del self.A[e]
            
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)