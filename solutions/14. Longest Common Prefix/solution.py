# Problem: Longest Common Prefix
# Language: python3
# Runtime: 28 ms
# Memory: 14.5 MB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        i = 0
        pre = ""
        while True:
            l = ""
            for w in strs:
                if not w or i >= len(w):
                    return pre
                if not l:
                    l = w[i]
                if w[i] != l:
                    return pre
            i+=1
            pre += l
        
        return pre