# Problem: Random Pick with Blacklist
# Language: python3
# Runtime: 3588 ms
# Memory: 30.8 MB

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        s = set(blacklist)
        self.N = N - len(s)
        key = [x for x in blacklist if x < N-len(blacklist)]
        val = [x for x in range(N-len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key,val))
    def pick(self) -> int:
        i = randint(0, self.N-1)
        return self.mapping.get(i, i)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()