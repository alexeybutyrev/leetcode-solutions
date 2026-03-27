# Problem: Word Break
# Language: python3
# Runtime: 39 ms
# Memory: 16.5 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        
        stack = [0]
        seen = {0}
        i = 0
        while stack:
            ind = stack.pop()
            for w in wordDict:
                nw = len(w)
                if ind + nw not in seen and s[ind:].startswith(w):
                    if ind + nw == N:
                        return True
                    stack.append(ind + nw)
                    seen.add(ind + nw)
        return False
            
                    