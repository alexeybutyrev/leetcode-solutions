# Problem: Concatenated Words
# Language: python3
# Runtime: 457 ms
# Memory: 30.8 MB

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        
        @cache
        def dfs(word):
            for i in range(1,len(word)):
                
                pre = word[:i]
                suf = word[i:]
                if (pre in s and suf in s) or (pre in s and dfs(suf)) or (suf in s and dfs(pre)):
                    return True
                
            return False
            
        ans = []
        for w in words:
            if dfs(w):
                ans.append(w)
        return ans