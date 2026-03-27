# Problem: Find Substring With Given Hash Value
# Language: python3
# Runtime: 530 ms
# Memory: 14.3 MB

class Node:
    def __init__(self):
        self.t = defaultdict(Node)
        self.val = 0

    def add(self, word: str, P, MOD) -> None:
        curr = self
        for i,l in enumerate(word):
            if l not in curr.t:
                v = curr.val + (ord(l) - ord('a') + 1) * pow(P, i, MOD)
                v %= MOD
                curr = curr.t[l]
                curr.val = v
            else:
                curr = curr.t[l]
        return curr.val
        
    def search(self, word: str, i = 0, curr = None) -> bool:
        # check if we at the end
        if i == len(word): return curr.iw
        # check if we started
        if not curr: return self.search(word, i, self)
        # .
        if word[i] == '.': return any(self.search(word,i+1, curr.t[l]) for l in curr.t)
        return self.search(word,i+1, curr.t[word[i]]) if word[i] in curr.t else False
    
class Solution:
    def subStrHash(self, S: str, P: int, MOD: int, k: int, hashValue: int) -> str:
        N = len(S)
        curr = 0
        val = lambda x: ord(x) - ord('a') + 1
        b = 1
        res = len(S)
        for i in range(N-1,-1,-1):
            curr = (curr * P + val(S[i])) % MOD
            if i + k >= N:
                b = b * P % MOD
            else:
                curr = (curr - val(S[i+k]) * b) % MOD
            if curr == hashValue:
                res = i
        return S[res:res + k]