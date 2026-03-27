# Problem: Word Break
# Language: python3
# Runtime: 24 ms
# Memory: 14.4 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        def replace(s, wd):
            #print(s)
            if not s:
                return True
            
            ns = len(s)
            for w in wd:
                nw = len(w)
                s0 = s
                
                while len(s0) >= nw and s0[0:nw] == w:
                    s0 = s0[nw:]
                    if s0 in wd:
                        return True
                if s0 != s and replace(s0,wd):
                    return True
            return False
                
        
        return replace(s, wordDict)